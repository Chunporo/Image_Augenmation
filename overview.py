import os
import glob

import numpy as np
import scipy as sp
import pandas as pd

from skimage.io import imread, imsave, imshow
from skimage.transform import rotate, AffineTransform, warp, rescale, resize, downscale_local_mean
from skimage import color, data
from skimage.exposure import adjust_gamma
from skimage.util import random_noise 

#OpenCV-Python
import cv2

# imgaug
import imageio
import imgaug as ia
import imgaug.augmenters as iaa

# Albumentations
import albumentations as A

# Augmentor
import Augmentor 

# Keras
from keras.preprocessing.image import ImageDataGenerator,array_to_img, img_to_array, load_img 

# SOLT
import solt
import solt.transforms as slt

#visualisation
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import seaborn as sns
from IPython.display import HTML, Image

#source: https://www.kaggle.com/jpmiller/nfl-punt-analytics/edit
# set additional display options for report
pd.set_option("display.max_columns", 100)
th_props = [('font-size', '13px'), ('background-color', 'white'), 
            ('color', '#666666')]
td_props = [('font-size', '15px'), ('background-color', 'white')]
styles = [dict(selector="td", props=td_props), dict(selector="th", 
            props=th_props)]

#warnings
import warnings
warnings.filterwarnings("ignore")


#Helper function to display the images in a grid
# Source: https://stackoverflow.com/questions/42040747/more-idiomatic-way-to-display-images-in-a-grid-with-numpy which was pointed by
# this excellent article: https://towardsdatascience.com/data-augmentation-for-deep-learning-4fe21d1a4eb9
def gallery(array, ncols=3):
    '''
    Function to arange images into a grid.
    INPUT:
        array - numpy array containing images
        ncols - number of columns in resulting imahe grid
    OUTPUT:
        result - reshaped array into a grid with given number of columns
    '''
    nindex, height, width, intensity = array.shape
    nrows = nindex//ncols
    assert nindex == nrows*ncols
    result = (array.reshape(nrows, ncols, height, width, intensity)
              .swapaxes(1,2)
              .reshape(height*nrows, width*ncols, intensity))
    return result

