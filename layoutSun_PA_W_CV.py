
import cv2 as cv
import numpy as np
import math

# The function generateSunLayout() generates an image of the sun's layout,
# taking as parameters the resolution of the image, the radius and center of the
# generated circle, the vector PA and the width W.

def generateSunLayout(imgResolution, cirCenter, r, PA, W):
    # Matrix of size imgResolution (px,px) filled with 1's. That matrix represents
    # the white background of the generated image.
    img = np.ones((imgResolution[0], imgResolution[1], 3), np.uint8) * 255

    # Circle with center in the cirCenter point. The function
    # cv.circle() receives the desired radius (r) of the circle as a parameter
    cv.circle(img, cirCenter, r, (255,0,0), 2, cv.LINE_AA)


    # x_PA , y_PA are the variables that locate the vector PA in the circle.
    x_PA = int(r * 1.3 * math.cos(3*math.pi/2 - PA*math.pi/180)) + cirCenter[0]
    y_PA = int(r * 1.3 * math.sin(3*math.pi/2 - PA*math.pi/180)) + cirCenter[1]

    # vector PA
    cv.arrowedLine(img, cirCenter, (x_PA, y_PA), (0,0,255), 2, tipLength = 0.05)

    # (x_upW, y_upW) and (x_downW, y_downW) locate W
    x_upW = int(r*1.3*math.cos((3*math.pi/2 - PA*math.pi/180) + W*math.pi/360)) + cirCenter[0]
    y_upW = int(r*1.3*math.sin(3*math.pi/2 - PA*math.pi/180 + W*math.pi/360)) + cirCenter[1]

    x_downW = int(r*1.3*math.cos((3*math.pi/2 - PA*math.pi/180) - W*math.pi/360)) + cirCenter[0]
    y_downW = int(r*1.3*math.sin(3*math.pi/2 - PA*math.pi/180 - W*math.pi/360)) + cirCenter[1]

    # lines that limits W area
    cv.line(img, cirCenter, (x_upW, y_upW), (0,0,0), 2, cv.LINE_AA)
    cv.line(img, cirCenter, (x_downW, y_downW), (0,0,0), 2, cv.LINE_AA)

    # the generated image is returned
    return img



# The main() function
def main():
    # Some parameters are defined to send them to the function
    imgResolution = (1000, 1000)
    cirCenter = (250, 500)
    r = 125
    PA = 115
    W = 60

    # The function generateSunLayout() return the generated image in the varible 'image'
    image = generateSunLayout(imgResolution, cirCenter, r, PA, W)

    # The generated image is displayed and saved
    cv.imshow('image', image)
    cv.imwrite('imagenGenerada.jpg', image)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
