import numpy as np
from h5py import File
from os.path import join
from .rBFs import rBFs
from scipy.special import eval_legendre as leg
from scipy.integrate import simpson

try:
	import dill
except:
	def cpu_count():
		return 1
else:
	from multiprocessing import Pool, cpu_count

	def packed_func(func_and_item):
		dumped_function, item = func_and_item
		target_function = dill.loads(dumped_function)
		res = target_function(item)
		return res

	def pack(target_function, items):
		dumped_function = dill.dumps(target_function)
		dumped_items = [(dumped_function, item) for item in items]
		return packed_func,dumped_items

def loadG(gData, make_images=False):

	if isinstance(gData, str):
		with File(gData, 'r') as gData:
			return loadG(gData, make_images)
	elif isinstance(gData, File):
		gData_dict = {}
		for key in ['y','x','nk','nl','Up','S','V','frk','l']+make_images*['Ginv']:
			gData_dict[key] = gData[key][()]
		return loadG(gData_dict, make_images)
	else:
		return gData

def get_gData(gData, save_path=None, save_dir=None, custom_rBF=None, nProc=cpu_count(), silent=0, shape='half'):
	if shape not in ['half', 'quadrant']:
		raise Exception(f"keyword shape ({shape}) must be either one of ['half', quadrant']")

	if not silent:
		print('Setting up calculations, using %d core(s)...' % nProc)

	# Set defaults.
	if save_path is None:
		save_path = '_'.join(['G','r'+str(len(gData['x'])),'k'+str(len(gData['k'])),'l'+str(max(gData['l']))])+f'_{shape}.h5'
	if save_dir is not None:
		save_path = join(save_dir, save_path)
	nProc = min(nProc, cpu_count())

	# Find problem dimension.
	gData['nk'] = len(gData['k'])
	gData['nl'] = len(gData['l'])

	# Load radial basis function and zero-integrand point function.
	if gData['rBF'] != 'custom':
		rBF = rBFs(gData['rBF'], custom_rBF)
	if len(rBF) == 1:
		rBF = rBF[0]
	if callable(rBF):
		zIP = 1.5*max(gData['x'])
		trapz_step = 0.05
	elif len(rBF) == 2:
		if callable(rBF[1]):
			rBF, zIP = rBF
			trapz_step = 0.1
		else:
			rBF, trapz_step = rBF
			zIP = 1.5*max(gData['x'])
	else:
		rBF, zIP, trapz_step = rBF
	rBF_2 = lambda x, k: rBF(x, k, gData['params'])
	zIP_2 = lambda x, k: zIP(x, k, gData['params'])

	if not silent:
		print('Sampling Abel transformed basis functions...')

	# Sample the Abel transformed basis functions.
	G = findG(gData['x'], gData['k'], gData['l'], rBF_2, zIP_2, trapz_step, nProc, shape=shape)
	if shape=='half':
		gData['y'] = np.concatenate((-gData['x'][::-1], gData['x']))
	elif shape=='quadrant':
		gData['y'] = gData['x'].copy()
	else:
		raise NameError(f"'shape' ({shape}) must be either 'quadrant' or 'half'")

	if not silent:
		print('Computing the singular value decomposition...')

	# Find the singular value decomposition of the G matrix for least-squares fitting.
	U, S, Vp = np.linalg.svd(G,0)
	gData['Up'], gData['S'], gData['V'] = U.T, S, Vp.T

	if not silent:
		print('Sampling the basis functions...')

	# Sample the radial basis functions.
	gData['frk'] = rBF_2(gData['x'], gData['k'])
	gData['Ginv'] = findGinv(gData['y'], gData['x'], gData['k'], gData['l'], rBF_2)

	if not silent:
		print('Saving results...')

	# Save the calculation results.
	with File(save_path,'w') as f:
		for key in gData.keys():
			f.create_dataset(key,data=gData[key])

	if not silent:
		print('Done!')

def findG(X, K, L, rBF, zIP, trapz_step, nProc=cpu_count()-1, shape='half'):
	nX = len(X)
	nK = len(K)
	nL = len(L)

	Y, X = np.meshgrid(X, X)
	Y, X = Y.flatten(), X.flatten()
	R = np.sqrt(X**2+Y**2)
	u = np.arange(0, max(zIP(0, K)), trapz_step)

	def findG_sub(yr):

		y, r = yr
		G_sub = np.zeros(len(K)*len(L))

		cos_term = np.nan_to_num(y/np.sqrt(u**2+r**2))
		leg_terms = np.zeros((len(L), len(u)))
		for i, l in enumerate(L):
			leg_terms[i] = leg(l, cos_term)

		for i, k in enumerate(K):
			u_sub = u[u<=zIP(r, k)]
			if u_sub.size:
				rad_term = rBF(np.sqrt(u_sub**2+r**2), k)
				G_sub[i::len(K)] = simpson(rad_term*leg_terms[:,:len(u_sub)], x=u_sub, dx=trapz_step)

		return G_sub

	if nProc > 1:
		p = Pool(nProc)
		G = p.map(*pack(findG_sub, zip(Y, R)))
		p.close()
	else:
		G = map(findG_sub, zip(Y, R))
	quadrant = np.array(list(G))/(2*np.pi)
	if shape=='half':
		quadrant = quadrant.reshape(nX, nX, nL, nK)
		parity = np.ones(shape=(nX, nX, nL, nK))
		parity[:,:,L%2==1,:] = -1
		completion = quadrant * parity
		full = np.concatenate((completion[:,::-1], quadrant), axis=1)
		full = full.reshape(nX*2 * nX, nK * nL)
	elif shape=='quadrant':
		full = quadrant

	return full


def findGinv(y, x, k, l, rBF):

	Y, X = np.meshgrid(y, x)
	Y, X = Y.flatten(), X.flatten()
	R = np.sqrt(X**2+Y**2)
	CosTh = Y/R

	Irk = rBF(R, k)
	Pl = np.empty((len(X), len(l)))
	for i, li in enumerate(l):
		Pl[:,i] = leg(li, CosTh)

	# for reshape, axes of (y, x, l, k)
	flattened = np.nan_to_num((Pl[:,:,None] * Irk[:,None]).reshape(len(X), -1), copy=False)
	reshaped = flattened.reshape(len(x), len(y), len(l), len(k))
	return flattened