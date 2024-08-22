'''
Current status: the image_shape='quadrant' option works (which is what pbasex
does). The image_shape='half' option doesn't work, code snippets are still
testing the behaviour of this option.
'''

# %%
import numpy as np
import time

# Settings
save_path = None # Automatic file naming if none
save_dir = None # Directory to save the data
nx = 256  # 512x256 half-image, or 256x256 quadrant
xkratio = 4 # Ratio of radial basis functions to pixel radii
l_values = np.arange(5) # Up to l=4
l_values = np.arange(0, 5, 2) # Up to l=4, even l only
k_spacing = 'linear' # Even pixel or energy bins
gData = {}
gData['rBF'] = 'gauss' # Gaussian basis function
image_shape = 'half'

# Set up the parameters
gData['x'] = np.arange(nx, dtype='double')-0.5 # we should have 0 = x[0] - 0.5*xstep 

if k_spacing=='linear':

	gData['k'] = np.arange(0, nx, xkratio) + 0.5 * (xkratio - 1)
	gData['params'] = 0.7 * xkratio # Gaussian width

elif k_spacing=='quadratic':

	gData['k'] = np.sqrt(np.linspace(0, (nx-1)**2, nx))
	gData['params'] = xkratio

gData['l'] = l_values

if gData['rBF'] == 'custom':

	def rBF(r, k, params):

		return 1/((r-k)**2+(params/2)**2) # Lorentzian basis function

	def zIP(r, k, params):

		return np.sqrt((np.sqrt(max(0, 10-(params/2)**2)) + k)**2 - r**2)

	trapz_step = 0.1

	custom_rBF = (rBF, zIP, trapz_step)

else:

	custom_rBF = None

np.seterr("ignore")

t0 = time.time()

from cpbasex import get_gData
get_gData(gData, save_path=save_path, save_dir=save_dir, custom_rBF=custom_rBF, nProc=1, shape='half')
# get_gData(gData, save_path="G_r256_k64_l4_quadrant.h5", save_dir=save_dir, custom_rBF=custom_rBF, nProc=1, shape='quadrant')

print(time.time()-t0, "seconds elapsed")