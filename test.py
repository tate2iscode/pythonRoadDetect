from ProcessingImage import *
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("datas/highway.jpeg", cv2.IMREAD_GRAYSCALE)
#img = process(img)
img = perspectiveTransform(img)
_, img = cv2.threshold(img, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print(img.shape)
cv2.imwrite("result/bevd.jpg", img)

y, x = img.shape

background = drawRect(img)
background = perspectiveTransform2(background)
#cv2.drawContours(background, contours, -1, (255, 255, 255))
cv2.imwrite("result/contours.jpg", background)
