import numpy as np
from quadrant import unfoldQuadrant
from .gData import loadG

def unfoldHalf(M):
	"""
	Unfold the image-half into a symmetric full image. Image completion along
	axis=0.
	"""
	return np.vstack((np.flipud(M),M))


def resizeFoldedHalf(M, r_max):
	"""
	Resize a half-folded image to a certain max radius. Final shape (r_max,
	2*r_max, ...).
	"""
	sx, sy = M.shape[:2]

	if sx > r_max: 
		x0, x1 = None, None
		x0_m, x1_m = 0, r_max
	else:
		x0, x1 = 0, sx
		x0_m, x1_m = None, None
	if sy>2*r_max:
		y0, y1 = None, None
		y0_m, y1_m = sy//2-r_max, sy//2+r_max
	else:
		y0, y1 = r_max-sy//2, r_max+sy//2
		y0_m, y1_m = None, None
	resized = np.zeros((r_max, 2*r_max) + M.shape[2:])
	resized[x0:x1, y0:y1] = M[x0_m:x1_m, y0_m:y1_m]

	return resized  # not sure if tranpose is a good solution

def foldHalf(M, x0=None, y0=None, half_filter=[1,1]):
	"""
	Fold the halves of a full image onto each other. Fold/Collapse along
	axis=0.
	"""

	default_big_int = 99999999
	hsigns = np.array([-1, 1])
	sy, sx = M.shape[:2]

	if x0 is None:
		x0 = int(sx/2)
	if y0 is None:
		y0 = int(sy/2)
	
	if (x0 < 0) or (x0 > sx):
		raise IndexError(f'keyword x0 ({x0}) is out of range. Value must lie between 0 and {sx}')

	if (y0 < 0) or (y0 > sy):
		raise IndexError(f'keyword y0 ({y0}) is out of range. Value must lie between 0 and {sy}')

	lx, ly = default_big_int, default_big_int

	# lx, ly will be the maximum centre-to-edge size, where no pixels are cut off
	if half_filter[0]:
		lx = min(lx, x0)
	if half_filter[1]:
		lx = min(lx, sx-x0)
	ly = min(ly, y0)
	ly = min(ly, sy-y0)
	
	Mout = np.zeros((lx, 2*ly) + M.shape[2:])

	for i in range(2):
		if half_filter[i]:
			xf = x0 + hsigns[i]*lx
			if xf == -1:
				xf = None
			Mout += M[x0:xf:hsigns[i], y0-ly:y0+ly]

	return Mout

def cpbasex(images, gData, make_images=False, weights=None, regularization=0, alpha=1.0, shape='half'):
	
	gData  = loadG(gData, make_images)
	ny, nx, nk, nl = len(gData['y']), len(gData['x']), gData['nk'], gData['nl']

	try:
		nim = images.shape[2]
	except:
		nim = 1
		images = images.reshape(nx, nx, nim)

	images = images.reshape(ny*nx,nim)

	if weights is None:
		c = gData['V'].dot((gData['S']/(gData['S']**2+regularization))[:,None]*(gData['Up'].dot(images)))

	else:
		weights = weights.flatten()
		c = gData['V'].dot((gData['S']/(gData['S']**2+regularization))[:,None]*(np.linalg.solve((gData['Up']*weights[None,:]).dot(gData['Up'].T),gData['Up'].dot(weights[:,None]*images))))

	E = alpha*gData['x']**2
	IEB = 1/(2*alpha)*np.diag(gData['x']).dot(gData['frk'].dot(c.reshape(nl,nk,nim).swapaxes(0,1).reshape(nk,nl*nim)))
	IE = IEB[:,:nim]
	with np.errstate(divide='ignore'):
		betas = IEB[:,nim:].reshape(nx,nl-1,nim)/IE[:,None,:]

	if make_images:
		if shape=='half':
			fit = unfoldHalf(gData['Up'].T.dot(np.diag((gData['S']**2+regularization)/gData['S']).dot(gData['V'].T.dot(c))).reshape(nx,ny,nim))
			inv = unfoldHalf(gData['Ginv'].dot(c).reshape(nx,ny,nim))

	if make_images:
		if shape=='quadrant':
			fit = unfoldQuadrant(gData['Up'].T.dot(np.diag((gData['S']**2+regularization)/gData['S']).dot(gData['V'].T.dot(c))).reshape(ny,nx,nim))
			inv = unfoldQuadrant(gData['Ginv'].dot(c).reshape(nx,ny,nim))

	out = {'E': E, 'IE': np.squeeze(IE), 'betas': np.squeeze(betas), 'c': np.squeeze(c)}
	if make_images:
		out['fit'], out['inv'] = np.squeeze(fit), np.squeeze(inv)

	return out
