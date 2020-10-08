# Chapter 3
# Resizing & Cropping
import cv2

# Default Image
img = cv2.imread('Resources/lena.png')
print(img.shape)
cv2.imshow('Image', img)

# Resize Image
imgResize = cv2.resize(img, (200,200))
print(imgResize.shape)
cv2.imshow('Resize Image', imgResize)

# Crop Image
imgCropped = img[0:150, 150:350]
cv2.imshow('Image Cropped', imgCropped)

cv2.waitKey(0)