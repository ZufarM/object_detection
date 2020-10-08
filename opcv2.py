# Chapter 2
# Basic Functions
import cv2
import numpy as np

img = cv2.imread('Resources/lena.png')
kernel = np.ones((5,5),np.uint8)

# Gray Image
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray Image', imgGray)

# Blur Image
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)
cv2.imshow('Blur Image', imgBlur)

# Canny Image
imgCanny = cv2.Canny(img, 150, 200)
cv2.imshow('Canny Image', imgCanny)

# Dialation Image
imgDialation = cv2.dilate(imgCanny,kernel, iterations=1)
cv2.imshow('Dialation Image', imgDialation)

# Eroded Image
imgEroded = cv2.erode(imgDialation,kernel, iterations=1)
cv2.imshow('Eroded Image', imgEroded)

cv2.waitKey(0)