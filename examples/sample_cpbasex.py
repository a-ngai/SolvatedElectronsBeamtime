'''
Current status: The many plot outputs are here to test the shape='half' option.
Still in progress
'''
# %%
import numpy as np
import matplotlib as mpl
# mpl.use('TKAgg')
import matplotlib.pyplot as plt
from cpbasex import pbasex, loadG
from quadrant import foldQuadrant, resizeFolded, unfoldQuadrant

def unfoldHalf(M):
	"""
	Unfold the image-half into a symmetric full image.
	"""

	return np.hstack((np.fliplr(M),M))

def resizeFoldedHalf(M, r_max):
	"""
	Resize a half-folded image to a certain max radius.
	"""

	sy,sx = M.shape[:2]

	if sx > r_max:
		x0, x1 = 0, r_max
	else:
		x0, x1 = r_max-sx, sx
	if sy>2*r_max:
		y0, y1 = 0, 2*r_max
		y0_m, y1_m = sy//2-r_max, sy//2+r_max
	else:
		y0, y1 = r_max-sy//2, r_max+sy//2
		y0_m, y1_m = None, None
	
	resized = np.zeros((2*r_max, r_max) + M.shape[2:])
	resized[y0:y1, x0:x1] = M[y0_m:y1_m, x0:x1]

	return resized

def foldHalf(M, x0=None, y0=None, half_filter=[1,1]):
	"""
	Fold the halves of a full image onto each other.
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
	
	Mout = np.zeros((2*ly,lx) + M.shape[2:])

	for i in range(2):
		if half_filter[i]:
			xf = x0 + hsigns[i]*lx
			if xf == -1:
				xf = None
			Mout += M[y0-ly:y0+ly, x0:xf:hsigns[i]]

	return Mout

# Load images

# samples = [
# 	'cpbasex_images/low_counts.bin',
# 	'cpbasex_images/high_counts.bin',
# 	'cpbasex_images/fancy.bin',
# 	'cpbasex_images/fancier.bin'
# 	]

samples = [
	'cpbasex_images/low_counts',
	'cpbasex_images/high_counts',
	'cpbasex_images/fancy',
	'cpbasex_images/fancier'
	]

raw = np.dstack(tuple(np.loadtxt(sample) for sample in samples))

# Fold images into half-images
x0, y0 = 128, 128
half_filter = [1,1]
half_folded = resizeFoldedHalf(foldHalf(raw, x0=x0, y0=y0, half_filter=half_filter), 128)

x0, y0 = 128, 128
quadrant_filter = [1,1,1,1]
quadrant_folded = resizeFolded(foldQuadrant(raw, x0=x0, y0=y0, quadrant_filter=quadrant_filter), 128)


# plt.imshow(foldHalf(raw, x0=x0, y0=y0, half_filter=half_filter)[:,:,3])
# plt.show()
# raise Exception

# Load inversion data
# gData = loadG('G_r128_k32_l4.h5', 1)

def invert(half_image, gData, regularization):
    nx, ny, nk, nl = len(gData['x']), len(gData['y']),  gData['nk'], gData['nl']
    image_half = half_image.reshape(nx*ny,1)
    c = gData['V'] @ ((gData['S']/(gData['S']**2+regularization))[:,None]*(gData['Up'].dot(image_half)))
    IEB = np.diag(gData['x']).dot(gData['frk'].dot(c.reshape(nl,nk).swapaxes(0,1).reshape(nk,nl)))
    IE = IEB[:,:1]
    betas = IEB[:,1:].reshape(nx,nl-1)/IE
    out = {'IE': np.squeeze(IE), 'betas': np.squeeze(betas), 'c': np.squeeze(c)}
    pes = out['IE'][:].reshape(-1,1)
    b = (out['betas'][:,:])
    return [pes, b]

import h5py

def load_gData(path_gData):
	gData = {}
	with h5py.File(path_gData, 'r') as gData_file:
		for key in ['x','nk','nl','Up','S','V','frk','Ginv']:
			gData[key] = gData_file[key][()] 

		try: 
			gData['y'] = gData_file['y'][()]
		except:
			gData['y'] = gData_file['x'][()]
	return gData



def cpbasex(images, gData, make_images=False, weights=None, regularization=0, alpha=1.0, shape='half'):
	
	gData  = loadG(gData, make_images)
	ny, nx, nk, nl = len(gData['y']), len(gData['x']), gData['nk'], gData['nl']
	# print(ny, nx, nk, nl)
	# print(np.shape(gData['Ginv']))

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
			fit = unfoldHalf(gData['Up'].T.dot(np.diag((gData['S']**2+regularization)/gData['S']).dot(gData['V'].T.dot(c))).reshape(ny,nx,nim))
			inv = unfoldHalf(gData['Ginv'].dot(c).reshape(nx,ny,nim).transpose(1,0,2))

	if make_images:
		if shape=='quadrant':
			fit = unfoldQuadrant(gData['Up'].T.dot(np.diag((gData['S']**2+regularization)/gData['S']).dot(gData['V'].T.dot(c))).reshape(ny,nx,nim))
			inv = unfoldQuadrant(gData['Ginv'].dot(c).reshape(nx,ny,nim))

	out = {'E': E, 'IE': np.squeeze(IE), 'betas': np.squeeze(betas), 'c': np.squeeze(c)}
	if make_images:
		out['fit'], out['inv'] = np.squeeze(fit), np.squeeze(inv)

	return out



plt.imshow(quadrant_folded[:,:,3])
plt.colorbar()
plt.show()

# pes, b = invert(folded[:,:,3], gData, 0)
# plt.plot(pes)
# plt.show()

# PBASEX part!
image_i = 0
if True:
	i = image_i
	print(f'pbasex, quadrant, image {i}')
	pbasex_gData = load_gData('G_r128_k32_l4_pbasex.h5')
	out = pbasex(quadrant_folded, pbasex_gData, make_images=True, weights=None, regularization=0, alpha=1.0)
	fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(1,5,figsize=(16,4))
	cax1 = ax1.imshow(raw[:,:,i])
	ax1.set_title('raw')
	cbar = fig.colorbar(cax1, ax=ax1)

	cax2 = ax2.imshow(out['inv'][:,:,i])
	ax2.set_title('inv')
	cbar = fig.colorbar(cax2, ax=ax2)

	cax3 = ax3.imshow(out['fit'][:,:,i] - unfoldQuadrant(quadrant_folded[:,:,i]))
	ax3.set_title('fit')
	cbar = fig.colorbar(cax3, ax=ax3)

	cax4 = ax4.imshow(pbasex_gData['Ginv'].reshape(
		len(pbasex_gData['y']), len(pbasex_gData['x']), pbasex_gData['nl'], pbasex_gData['nk'])[:,:,1,10]
		)
	cbar = fig.colorbar(cax4, ax=ax4)

	pbasex_G = pbasex_gData['Up'].T @ np.diag(pbasex_gData['S']) @ pbasex_gData['V'].T
	reshaped_G = pbasex_G.reshape(len(pbasex_gData['y']), len(pbasex_gData['x']), pbasex_gData['nl'], pbasex_gData['nk'])
	print(np.shape(pbasex_G))
	ax5.imshow(reshaped_G[:,:,2,11])

	plt.show()

if True:
	i = image_i
	print(f'cpbasex, quadrant, image {i}')
	cpbasex_gData = load_gData('G_r128_k32_l4_quadrant.h5')
	out = cpbasex(quadrant_folded, cpbasex_gData, make_images=True, weights=None, regularization=0, alpha=1.0, shape='quadrant')
	fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(1,5,figsize=(16,4))
	cax1 = ax1.imshow(raw[:,:,i])
	ax1.set_title('raw')
	cbar = fig.colorbar(cax1, ax=ax1)

	cax2 = ax2.imshow(out['inv'][:,:,i])
	ax2.set_title('inv')
	cbar = fig.colorbar(cax2, ax=ax2)

	cax3 = ax3.imshow(out['fit'][:,:,i] - unfoldQuadrant(quadrant_folded[:,:,i]))
	ax3.set_title('fit')
	cbar = fig.colorbar(cax3, ax=ax3)

	cax4 = ax4.imshow(cpbasex_gData['Ginv'].reshape(
		len(cpbasex_gData['y']), len(cpbasex_gData['x']), cpbasex_gData['nl'], cpbasex_gData['nk'])[:,:,1,10]
		)
	cbar = fig.colorbar(cax4, ax=ax4)

	cpbasex_G = cpbasex_gData['Up'].T @ np.diag(cpbasex_gData['S']) @ cpbasex_gData['V'].T
	reshaped_G = cpbasex_G.reshape(len(cpbasex_gData['y']), len(cpbasex_gData['x']), cpbasex_gData['nl'], cpbasex_gData['nk'])
	print(np.shape(cpbasex_G))
	ax5.imshow(reshaped_G[:,:,2,11])
	plt.show()

if True:
	i = image_i
	print(f'cpbasex, half, image {i}')
	cpbasex_gData = load_gData('G_r128_k32_l4.h5')
	out = cpbasex(half_folded, cpbasex_gData, make_images=True, weights=None, regularization=0, alpha=1.0, shape='half')
	fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(1,5,figsize=(16,4))
	cax1 = ax1.imshow(raw[:,:,i])
	ax1.set_title('raw')
	cbar = fig.colorbar(cax1, ax=ax1)

	cax2 = ax2.imshow(out['inv'][:,:,i])
	ax2.set_title('inv')
	cbar = fig.colorbar(cax2, ax=ax2)

	cax3 = ax3.imshow(out['fit'][:,:,i] - unfoldHalf(half_folded[:,:,i]))
	ax3.set_title('fit')
	cbar = fig.colorbar(cax3, ax=ax3)

	cax4 = ax4.imshow(cpbasex_gData['Ginv'].reshape(
		len(cpbasex_gData['x']), len(cpbasex_gData['y']), cpbasex_gData['nl'], cpbasex_gData['nk'])[:,:,1,10]
		)
	cbar = fig.colorbar(cax4, ax=ax4)

	cpbasex_G = cpbasex_gData['Up'].T @ np.diag(cpbasex_gData['S']) @ cpbasex_gData['V'].T
	reshaped_G = cpbasex_G.reshape(len(cpbasex_gData['x']), len(cpbasex_gData['y']), cpbasex_gData['nl'], cpbasex_gData['nk'])
	ax5.imshow(reshaped_G[:,:,2,11])
	plt.show()



raise Exception

folded = quadrant_folded

### CPBasex code, won't use this.

gData = loadG('G_r128_k32_l4.h5', 1)

# Apply the pBASEX algorithm
out = pbasex(folded, gData, make_images=True, alpha=4.1e-5)

# Plot some results
plt.figure(figsize=(12,9))
for i, sample in enumerate(samples):
	plt.subplot(4,5,5*i+1)
	plt.imshow(raw[:,:,i])
	plt.xticks([])
	plt.yticks([])
	plt.ylabel(sample)
	clim = plt.gci().get_clim()
	plt.clim(0,clim[1])
	if i==0:
		plt.title('Raw Image')
	plt.subplot(4,5,5*i+2)
	plt.plot(out['E'], out['IE'][:,i], 'k')
	plt.gca().ticklabel_format(axis='y', style='sci', scilimits=(-2,2))
	if i==3:
		plt.xlabel('Energy (eV)')
	plt.gca().twinx()
	plt.plot(out['E'], out['betas'][:,:,i], '.', markersize=5, alpha=0.6)
	if i==0:
		plt.text(-3, 3.5, 'counts per eV', size='small')
		plt.text(12, 3.5, 'beta', size='small')
		plt.text(3.5, 3.25, 'I(E), ', color='black', size='large')
		plt.text(6, 3.25, 'B2', color=u'#1f77b4', size='large')
		plt.text(7.5, 3.25, ', ', color='black', size='large')
		plt.text(8, 3.25, 'B4', color=u'#ff7f0e', size='large')
	plt.ylim(-1,3)
	plt.subplot(4,5,5*i+3)
	plt.imshow(out['fit'][:,:,i]/4)
	plt.xticks([])
	plt.yticks([])
	plt.clim(0,clim[1])
	if i==0:
		plt.title('Fitted Image')
	plt.subplot(4,5,5*i+4)
	plt.imshow(out['fit'][:,:,i]/4-raw[:,:,i])
	plt.xticks([])
	plt.yticks([])
	if i==0:
		plt.title('Fit Residual')
	plt.subplot(4,5,5*i+5)
	plt.imshow(out['inv'][:,:,i]/4)
	plt.xticks([])
	plt.yticks([])
	plt.clim(0,clim[1]/10)
	if i==0:
		plt.title('Inverted Image')
plt.tight_layout()
plt.show()
