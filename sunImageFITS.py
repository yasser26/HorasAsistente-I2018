import cv2 as cv
import numpy as np
import math
import glob
import os
import matplotlib.pyplot as plt

from astropy.io import fits


# The main() function
def main():
    fits_image_filename = 'ImageFITS/4.fits'
    sunImageFile = fits.open(fits_image_filename)

    sunImageFile.info()

#    print (sunImageFile[0].data.shape)
#    image_data = fits.getdata(fits_image_filename)

    cv.imwrite('PruebaFITS.jpeg', sunImageFile[0].data)

    sunImageFile.close()

if __name__ == '__main__':
    main()
