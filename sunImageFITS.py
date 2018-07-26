#import cv2 as cv
import numpy as np
import math
import glob
import os

from astropy.io import fits


# The main() function
def main():
    fits_image_filename = '1.fits'
    sunImageFile = fits.open(fits_image_filename)

    sunImageFile.info()

    print sunImageFile[0].header


if __name__ == '__main__':
    main()
