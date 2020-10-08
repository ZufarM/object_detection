# Chapter 4
# Shapes & Texts
import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
red = (0, 0, 255) # BGR
green = (0, 255, 0) # BGR
blue = (255, 0, 0) # BGR
shadeBlue = (255, 255, 0) # BGR
# print(img)
# img[0:150, 150:350] = color

cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), green, 3)
cv2.rectangle(img, (0, 0), (250, 250), blue, 3)
cv2.circle(img, (400, 50), 30, shadeBlue, 5)
cv2.putText(img, "  OPEN CV  ", (300, 200), cv2.FONT_HERSHEY_COMPLEX, 1, red, 3)

cv2.imshow('Image', img)
cv2.waitKey(0)