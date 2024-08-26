# %%
import numpy as np
import matplotlib as mpl
# mpl.use('TKAgg')
import matplotlib.pyplot as plt
from cpbasex import pbasex, loadG
from cpbasex import cpbasex, unfoldHalf, resizeFoldedHalf, foldHalf
from quadrant import foldQuadrant, resizeFolded, unfoldQuadrant
import h5py

_debug = False


# Load images
samples = [
	'cpbasex_images/low_counts',
	'cpbasex_images/high_counts',
	'cpbasex_images/fancy',
	'cpbasex_images/fancier'
	]

raw = np.dstack(tuple(np.loadtxt(sample) for sample in samples))

# Fold images into half-images
x0, y0 = 256, 256
half_filter = [1,1]
half_folded = resizeFoldedHalf(foldHalf(raw, x0=x0, y0=y0, half_filter=half_filter), 256)

x0, y0 = 256, 256
quadrant_filter = [1,1,1,1]
quadrant_folded = resizeFolded(foldQuadrant(raw, x0=x0, y0=y0, quadrant_filter=quadrant_filter), 256)

# Load inversion data

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


image_i = 0
if _debug and False:
	i = image_i
	print(f'cpbasex, quadrant, image {i}')
	cpbasex_gData = load_gData('G_r256_k64_l4_quadrant.h5')
	out = cpbasex(quadrant_folded, cpbasex_gData, make_images=True, weights=None, regularization=0, alpha=1.0, shape='quadrant')
	fig, (ax1, ax2, ax3, ax4, ax5, ax6) = plt.subplots(1,6,figsize=(20,4))
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

	cax6 = ax6.imshow(quadrant_folded[:,:,0])
	cbar = fig.colorbar(cax6, ax=ax6)

	plt.show()

if _debug and True:
	i = image_i
	print(f'cpbasex, half, image {i}')
	cpbasex_gData = load_gData('G_r256_k64_l4_half.h5')
	out = cpbasex(half_folded, cpbasex_gData, make_images=True, weights=None, regularization=0, alpha=1.0, shape='half')
	fig, (ax1, ax2, ax3, ax4, ax5, ax6) = plt.subplots(1,6,figsize=(20,4))
	cax1 = ax1.imshow(raw[:,:,i])
	ax1.set_title('raw')
	cbar = fig.colorbar(cax1, ax=ax1)

	cax2 = ax2.imshow(out['inv'][:,:,i])
	ax2.set_title('inv')
	cbar = fig.colorbar(cax2, ax=ax2)

	cax3 = ax3.imshow(out['fit'][:,:,i] - unfoldHalf(half_folded[:,:,i]))
	# cax3 = ax3.imshow(out['fit'][:,:,i])
	ax3.set_title('fit')
	cbar = fig.colorbar(cax3, ax=ax3)

	cax4 = ax4.imshow(cpbasex_gData['Ginv'].reshape(
		len(cpbasex_gData['x']), len(cpbasex_gData['y']), cpbasex_gData['nl'], cpbasex_gData['nk'])[:,:,1,10]
		)
	cbar = fig.colorbar(cax4, ax=ax4)

	cpbasex_G = cpbasex_gData['Up'].T @ np.diag(cpbasex_gData['S']) @ cpbasex_gData['V'].T
	reshaped_G = cpbasex_G.reshape(len(cpbasex_gData['x']), len(cpbasex_gData['y']), cpbasex_gData['nl'], cpbasex_gData['nk'])
	ax5.imshow(reshaped_G[:,:,2,11])

	cax6 = ax6.imshow(half_folded[:,:,0])
	cbar = fig.colorbar(cax6, ax=ax6)

	plt.show()

folded = half_folded

gData = load_gData('G_r256_k64_l4_half.h5')

# Apply the pBASEX algorithm
out = cpbasex(folded, gData, make_images=True, alpha=4.1e-5, shape='half')

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
		# plt.text(-3, 3.5, 'counts per eV', size='small')
		# plt.text(12, 3.5, 'beta', size='small')
		# plt.text(3.5, 3.25, 'I(E), ', color='black', size='large')
		# plt.text(6, 3.25, 'B2', color=u'#1f77b4', size='large')
		# plt.text(7.5, 3.25, ', ', color='black', size='large')
		# plt.text(8, 3.25, 'B4', color=u'#ff7f0e', size='large')
		pass
	plt.ylim(-1,3)
	plt.subplot(4,5,5*i+3)
	plt.imshow(out['fit'][:,:,i]/2)
	plt.xticks([])
	plt.yticks([])
	plt.clim(0,clim[1])
	if i==0:
		plt.title('Fitted Image')
	plt.subplot(4,5,5*i+4)
	plt.imshow(out['fit'][:,:,i]/2-raw[:,:,i])
	plt.xticks([])
	plt.yticks([])
	if i==0:
		plt.title('Fit Residual')
	plt.subplot(4,5,5*i+5)
	plt.imshow(out['inv'][:,:,i]/2)
	plt.xticks([])
	plt.yticks([])
	plt.clim(0,clim[1]/5)
	if i==0:
		plt.title('Inverted Image')
plt.tight_layout()
plt.show()
