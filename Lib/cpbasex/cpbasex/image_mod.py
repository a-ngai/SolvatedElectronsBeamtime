from warnings import warn
from fermi_libraries.common_functions import rebinning
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage.interpolation import rotate as scipy_rot
from scipy.ndimage import zoom
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
gist_heat = cm.get_cmap('gist_heat', 100)
hot_cmap = ListedColormap(np.flipud(gist_heat(range(100)))**0.3)

def find_center(image, center_guess, r_max, show_image = False): 
    """
    It takes as input:
    - image: an image
    - center_guess: a list of 2 elements with the initial guess for the position of the center. The first element is the center along the first dimension of image (raw), the second element is the center along the second dimension of the image (column).
    - r_max: a maximum distance from center_guess. The function will find the center of the image only looking at the image for r < rmax.
    It returns:
    - ouput = [center_raw_pix, center_col_pix]: a list of 2 elements with the retrieved center. The first element is the center along the raw axis, the second element is the center along the column axis. center_raw and center_col are two integers, defined such that:
        - image[:center_raw, :center_col] is the upper left quadrant
        - image[:center_raw, center_col:] is the upper right quadrant
        - image[center_raw:, :center_col] is the lower left quadrant
        - image[center_raw:, center_col:] is the lower right quadrant
    """
    
    image_copy = image.copy()
    nr, nc = np.shape(image)
    raw_i = np.arange(nr) - center_guess[0] + 0.5
    col_i = np.arange(nc) - center_guess[1] + 0.5
    Raw_i, Col_i = np.meshgrid(raw_i, col_i)
    R = np.sqrt(Raw_i**2 + Col_i**2)
    mask_out = R > r_max
    image_copy[mask_out] = 0

    dim_raw, dim_col = np.shape(image_copy)
    size = dim_raw
    xcorr_raw = []
    xcorr_col = []
    image_abs = (image_copy.copy())
    for jj in np.array((range(dim_raw))):
        jj_shift = int(jj - dim_raw/2)
        lapl_1 = image_abs
        lapl_2 = image_abs
        lapl_1 = np.roll(np.flipud(lapl_1), jj_shift, 0)
        if jj_shift >= 0:
            lapl_1[:jj_shift,:] = 0
        else:
            lapl_1[jj_shift:,:] = 0
        prod = np.sum(lapl_1 * lapl_2)
        xcorr_raw.append(prod)
    
        lapl_1 = image_abs
        lapl_2 = image_abs
        lapl_1 = np.roll(np.fliplr(lapl_1), jj_shift, 1)
        if jj_shift >= 0:
            lapl_1[:,:jj_shift] = 0
        else:
            lapl_1[:,jj_shift:] = 0
        prod = np.sum(lapl_1 * lapl_2)
        xcorr_col.append(prod)
    
    center_raw = +(np.argmax(xcorr_raw) - dim_raw/2 )/2 + dim_raw/2
    center_col = +(np.argmax(xcorr_col) - dim_col/2 )/2 + dim_col/2 
    center_raw_pix  = int(np.round(center_raw+0.5))
    center_col_pix  = int(np.round(center_col+0.5))
    
    output = [center_raw_pix, center_col_pix]
    x = np.linspace(center_guess[1] - r_max, center_guess[1] + r_max,101)
    y_u = center_guess[0] + np.sqrt(-(x - center_guess[1])**2 + r_max**2)
    y_d = center_guess[0] - np.sqrt(-(x - center_guess[1])**2 + r_max**2)
    if show_image:
        plt.figure(figsize = (8,3))
        plt.subplot(1,3,1)
        plt.imshow(image, cmap = hot_cmap)
        plt.plot( output[0], output[1],'.', markersize = '10', color = 'red')
        plt.plot(x,y_u, color = 'black', linewidth = 1, alpha = 0.5)
        plt.plot(x,y_d, color = 'black', linewidth = 1, alpha = 0.5)
        
        # check center by summing along x and y 
	
        plt.subplot(1,3,2)
        plt.plot(np.sum(image[:, output[1]:],0), label = 'right')
        plt.plot(np.flip(np.sum(image[:, :output[1]],0)), label = 'left')
        plt.title('left vs right')
        plt.subplot(1,3,3)
        plt.plot(np.sum(image[output[0]:, :],1), label = 'down')
        plt.plot(np.flip(np.sum(image[:output[0], :],1)), label = 'up')
        plt.title('up vs down')
        plt.tight_layout()
    print('center found at: ' + str(output))
    return output

def center_image(image, center, show_image=False):
    """
    Takes an image (image) and center (center) and returns the centered image.
    Center is a list of two elements, the first element is the center along the 1st dimension, the second element is the center along the 2nd dimension of the image.
    """
    size_raw, size_col = np.shape(image)
    diff_center_raw = int(size_raw/2) - center[0] 
    diff_center_col = int(size_col/2) - center[1] 
    image_centered = np.roll(image,diff_center_raw,0)
    image_centered = np.roll(image_centered,diff_center_col,1)
    if show_image:
        plt.figure(figsize = (8,3))
        plt.imshow(image, cmap = hot_cmap)
        plt.plot( 450, 450,'.', markersize = '10', color = 'red')
        print('center now at: ' + str([450, 450]))
    return image_centered

from scipy.ndimage.interpolation import shift
def center_image_interp(image, center, show_image=False):
    dim = np.shape(image)
    image = shift(image, (-center[0]+dim[0]/2,-center[1] + dim[1]/2))
    if show_image:
        plt.figure(figsize = (8,3))
        plt.imshow(image, cmap = hot_cmap)
        plt.plot( 450, 450,'.', markersize = '10', color = 'red')
        print('center now at: ' + str([450, 450]))
    return image
    
def rotate(image, angle, show_image = False):
    img_rot = scipy_rot(image, angle, reshape = False)
    if show_image:
        plt.figure(figsize = (8,3))
        plt.imshow(img_rot, cmap = hot_cmap)
        plt.plot( 450, 450,'.', markersize = '10', color = 'red')
    return img_rot

def zoom_horizontal(image, factor, show_image = False):
    if factor == 1:
        img_zoom = image
    else: 
        img_zoom = zoom(image, (1, factor), grid_mode = True)
        size_in = np.shape(image)
        size_out = np.shape(img_zoom)
        if factor > 1:
            size_1_diff = int(np.ceil((size_out[1] - size_in[1])/2))
            img_zoom = img_zoom[:,size_1_diff:size_1_diff+size_in[1]]
        if factor < 1:
            img_new = np.zeros(size_in)
            size_1_diff = int(np.floor((-size_out[1] + size_in[1])/2))
            img_new[:,size_1_diff:size_1_diff+size_out[1]] = img_zoom
            img_zoom = img_new
    if show_image:
        plt.figure(figsize = (8,3))
        plt.imshow(img_zoom, cmap = hot_cmap)
        plt.plot( 450, 450,'.', markersize = '10', color = 'red')
    return img_zoom

def stretch(image, stretch=(1,1), axis=(0,1)):
    if len(axis)!=2:
        raise ValueError(f'axis keyword {axis} must have length two')
    if len(stretch)!=2:
        raise ValueError(f'stretch keyword {stretch} must have length two')
    
    old_Nx, old_Ny, *_ = np.array(image.shape)[np.array(axis)]
    old_x, old_y = np.arange(old_Nx)-old_Nx//2, np.arange(old_Ny)-old_Ny//2
    stretched = image.copy()
    for zoom_factor, axis_i in zip(stretch, axis):
        zoom_factors = [1,]*image.ndim
        zoom_factors[axis_i] = zoom_factor
        stretched = zoom(stretched, zoom_factors)
    new_Nx, new_Ny = stretched.shape
    new_x, new_y = np.arange(new_Nx)-new_Nx//2, np.arange(new_Ny)-new_Ny//2
    stretched = rebinning(old_x, new_x, stretched, axis=axis[0])
    stretched = rebinning(old_y, new_y, stretched, axis=axis[1])
    return stretched

def find_rotation(image, guess=None):
    '''
    Find rotation in degrees.
    '''
    warn("rotation detection not implemented, returning trivial")
    rotation = 0
    return rotation

def find_ellipticity(image, guess=None):
    '''
    Find the ellipticity of the image.
    '''
    warn("ellipticity detection not implemented, returning trivial")
    ellipticity = np.array([1, 1])
    return ellipticity

def resize(image, new_N, axis=(0,1)):
    '''
    Resize the image using the rebinning() function.
    '''
    if len(new_N) != len(axis):
        raise ValueError(f'length of new_N ({len(new_N)})')
    old_shape = np.array(image.shape)
    reduced = image.copy()
    new_shape = np.array(old_shape)
    new_shape[np.array(axis)] = new_N
    old_N = old_shape[np.array(axis)]
    for old_N_i, new_N_i, axis_i in zip(old_N, new_N, axis):
        old_x = np.arange(old_N_i)
        new_x = np.linspace(0, old_N_i-1, num=new_N_i)
        reduced = rebinning(new_x, old_x, reduced, axis=axis_i)
    return reduced

def unfoldHalf(M):
	"""
	Unfold the image-half into a symmetric full image. Image completion along
	axis=0.
	"""
	return np.vstack((np.flipud(M),M))


def resizeFoldedHalf(M, r_max):
	"""
	Resize a half-folded image. Final shape (r_max,
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