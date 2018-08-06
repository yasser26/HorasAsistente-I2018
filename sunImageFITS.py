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


    image_data = fits.getdata('ImageFITS/5.fits', ext=0)
    print(image_data.shape)

    plt.figure()
    plt.imshow(image_data)
    plt.colorbar()
    plt.savefig("outFitsImagePLT.png")

    cv.imwrite('outFitsImageCV.png', sunImageFile[0].data)

    sunImageFile.close()

if __name__ == '__main__':
    main()
