# %%
"""
Run this to get the Abel inversion data. 

**Multi-threading**: Note that when running the get_gData() function, the nProc
keyword determines how many CPU cores will be used in parallel. If more than
one is used, there is a chance that Windows Defender will randomly cause them
to freeze! So if you see a large CPU usage from Windows Defenter or some other
antivirus program, it's better to restart this program and use only one core.
"""

# %%
import os
import time
import pathlib
import numpy as np
from cpbasex.gData import get_gData
from fermi_libraries.common_functions import resolve_path

# %%
try:
    CURRENT_SCRIPT_DIR = str(pathlib.Path(__file__).parent.resolve())+'/'
except NameError:  # this will happen in .ipynb files
    CURRENT_SCRIPT_DIR = os.path.abspath('')

# %%
# Settings

INVERSION_FOR_HALF_IMAGES = True
INVERSION_FOR_QUADRANT_IMAGES = False

save_half_path = None # Automatic file naming if none
save_quar_path = None # Automatic file naming if none
save_dir = resolve_path(CURRENT_SCRIPT_DIR, '../..') # Directory to save the data
nx = 225  # 512x225 half-image, or 225x225 quadrant
xkratio = 4 # Ratio of radial basis functions to pixel radii
l_values = np.arange(5) # Up to l=4
l_values = np.arange(0, 5, 2) # Up to l=4, even l only
gData = {}
gData['rBF'] = 'gauss' # Gaussian basis function

# %%
# Set up the parameters
gData['x'] = np.arange(nx, dtype='double')+0.5 # we should have 0 = x[0] - 0.5*xstep 

# linear k-spacing
gData['k'] = np.arange(0, nx, xkratio) + 0.5 * (xkratio - 1)
gData['params'] = 0.7 * xkratio # Gaussian width
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

if INVERSION_FOR_HALF_IMAGES:
	print('Setting up CPBASEX for half-images')
	get_gData(gData, save_path=save_half_path, save_dir=save_dir, custom_rBF=custom_rBF, nProc=1, shape='half')
	print('CPBASEX for half-images completed!')
	print()

if INVERSION_FOR_QUADRANT_IMAGES:
	print('Setting up CPBASEX for quarter-images')
	get_gData(gData, save_path=save_quar_path, save_dir=save_dir, custom_rBF=custom_rBF, nProc=1, shape='quadrant')
	print('Setting up CPBASEX for quarter-completed!')
	print()

print(time.time()-t0, "seconds elapsed")