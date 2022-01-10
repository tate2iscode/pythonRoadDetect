import cv2
import numpy as np
import matplotlib.pyplot as plt

def process(img):
    y, x = img.shape
    pt1 = np.array([[0, 0], [x, 0], [0, y]], np.int32)
    pt2 = np.array([[0, 0], [x, y], [x, 0]], np.int32)
    img = cv2.fillConvexPoly(img, pt1, (0, 0, 0))
    img = cv2.fillConvexPoly(img, pt2, (0, 0, 0))
    return img

def perspectiveTransform(img):
    y, x = img.shape
    half_x = int(round(x / 2))
    half_y = int(round(y / 2))
    value = 90
    pt1 = np.float32([[half_x-value, half_y], [half_x+value, half_y], [0, y], [x, y]])
    pt2 = np.float32([[0, 0], [x, 0], [0, y], [x, y]])
    M = cv2.getPerspectiveTransform(pt1, pt2)
    dst = cv2.warpPerspective(img, M, (x, y))
    return dst

def perspectiveTransform2(img):
    y, x = img.shape
    half_x = int(round(x / 2))
    half_y = int(round(y / 2))
    value = 75
    pt1 = np.float32([[0, 0], [x, 0], [0, y], [x, y]])
    pt2 = np.float32([[half_x - value, half_y], [half_x + value, half_y], [0, y], [x, y]])
    M = cv2.getPerspectiveTransform(pt1, pt2)
    dst = cv2.warpPerspective(img, M, (x, y))
    return dst

def BEVDProcess(img):
    y, x = img.shape
    #print(img.shape)

    #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #img = cv2.GaussianBlur(img, (5, 5), 0)
    _, img = cv2.threshold(img, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    return img

def drawRect(img):
    y, x = img.shape
    contours, _ = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    result = np.zeros([y, x])
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        print(w)
        if 10 < w < 50:
            cv2.rectangle(result, (x, y), (x + w, y + h), (255, 255, 255), 2)
    return result




















