import numpy as np
from quadrant import unfoldQuadrant
from .gData import loadG
from .image_mod import unfoldHalf

def cpbasex_energy(images, gData, make_images=False, weights=None, regularization=0, alpha=1.0, shape='half'):
	
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

def cpbasex(images, gData, make_images=False, weights=None, regularization=0, shape='half'):
	"""
	This gives the inversion in radial coordinates.
	"""
	
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

	r = gData['x']
	IRB = gData['frk'].dot(c.reshape(nl,nk,nim).swapaxes(0,1).reshape(nk,nl*nim))
	IR = IRB[:,:nim]
	with np.errstate(divide='ignore'):
		betas = IRB[:,nim:].reshape(nx,nl-1,nim)/IR[:,None,:]

	if make_images:
		if shape=='half':
			fit = unfoldHalf(gData['Up'].T.dot(np.diag((gData['S']**2+regularization)/gData['S']).dot(gData['V'].T.dot(c))).reshape(nx,ny,nim))
			inv = unfoldHalf(gData['Ginv'].dot(c).reshape(nx,ny,nim))

	if make_images:
		if shape=='quadrant':
			fit = unfoldQuadrant(gData['Up'].T.dot(np.diag((gData['S']**2+regularization)/gData['S']).dot(gData['V'].T.dot(c))).reshape(ny,nx,nim))
			inv = unfoldQuadrant(gData['Ginv'].dot(c).reshape(nx,ny,nim))

	out = {'r': r, 'IR': np.squeeze(IR), 'betas': np.squeeze(betas), 'c': np.squeeze(c)}
	if make_images:
		out['fit'], out['inv'] = np.squeeze(fit), np.squeeze(inv)

	return out

