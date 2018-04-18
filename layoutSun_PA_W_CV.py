

import cv2 as cv
import numpy as np
import math

def main():

    imgResolution = (600, 600)
    cirCenter = (300, 300)
    r = 50
    PA = 0
    W = 90

    img = np.ones((imgResolution[0], imgResolution[1], 3), np.uint8) * 255

    print img

    cv.circle(img, cirCenter, r, (255,0,0), 2, cv.LINE_AA)



    x_PA = int(r*1.3*math.cos(3*math.pi/2-PA*math.pi/180)) + cirCenter[0]
    y_PA = int(r*1.3*math.sin(3*math.pi/2-PA*math.pi/180)) + cirCenter[1]

    cv.arrowedLine(img, cirCenter, (x_PA, y_PA), (0,0,255), 2, tipLength = 0.05)

    x_upW = int(r*1.3*math.cos(3*math.pi/2 - PA*math.pi/180 - W*math.pi/360)) + cirCenter[0]
    y_upW = int(r*1.3*math.cos(3*math.pi/2 - PA*math.pi/180 + W*math.pi/360)) + cirCenter[1]

    x_downW = int(r*1.3*math.cos(3*math.pi/2 - PA*math.pi/180 + W*math.pi/360)) + cirCenter[0]
    y_downW = int(r*1.3*math.cos(3*math.pi/2 - PA*math.pi/180 - W*math.pi/360)) + cirCenter[1]

    cv.line(img, cirCenter, (x_upW, y_upW), (0,0,0), 2)
    cv.line(img, cirCenter, (x_downW, y_downW), (0,0,0), 2)



    cv.imshow('image', img)
    print(img.shape)
    cv.imwrite('imagenGenerada.jpg', img)
    cv.waitKey(0)
    cv.destroyAllWindows()





if __name__ == '__main__':
    main()
