import numpy as np
import cv2


def getCircles(img,parm1,parm2,minSize,maxSize):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    gray = cv2.medianBlur(gray, 3)
    lap = cv2.Laplacian(gray,cv2.CV_64F)
    # Calculate the sharpened image
    sharp = gray - 0.7*lap
    sharp = cv2.normalize(src=sharp, dst=None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
    rows = gray.shape[0]
    circles = cv2.HoughCircles(sharp, cv2.HOUGH_GRADIENT, 1, rows / 8,
                               param1=parm1, param2=parm2,
                               minRadius=minSize, maxRadius=maxSize)

    centers = []
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            centers.append(center)
            # circle center
            cv2.circle(sharp, center, 1, (0, 100, 100), 3)
            # circle outline
            radius = i[2]
            cv2.circle(sharp, center, radius, (255, 0, 255), 3)
    return sharp, centers


def getCircleCenters(img):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    gray = cv2.medianBlur(gray, 5)


    rows = gray.shape[0]
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 8,
                               param1=30, param2=20,
                               minRadius=int(rows*0.02), maxRadius=int(rows*0.07))

    x = []
    y = []
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            x.append(i[0])
            y.append(i[1])

    return x,y
