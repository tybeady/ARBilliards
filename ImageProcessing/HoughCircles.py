import numpy as np
import cv2

def getCircles(img):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    gray = cv2.medianBlur(gray, 5)


    rows = gray.shape[0]
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 8,
                               param1=30, param2=20,
                               minRadius=int(rows*0.01), maxRadius=int(rows*0.05))


    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            # circle center
            cv2.circle(img, center, 1, (0, 100, 100), 3)
            # circle outline
            radius = i[2]
            cv2.circle(img, center, radius, (255, 0, 255), 3)

    return img


def getCircleCenters(img):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    gray = cv2.medianBlur(gray, 5)


    rows = gray.shape[0]
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 8,
                               param1=30, param2=20,
                               minRadius=int(rows*0.01), maxRadius=int(rows*0.05))

    x = []
    y = []
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            x.append(i[0])
            y.append(i[1])

    return x,y
