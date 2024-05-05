import os
import cv2
import numpy as np

img = cv2.imread(os.path.join('.', 'data/michealjordan.jpg'))

resized_img = cv2.resize(img, (480, 360))

img_edge = cv2.Canny(resized_img, 50, 200)

# kenarlari kalinlastirir. 2,2 3,3 4,4 arttikca kalinlik artar
img_edge_dilate = cv2.dilate(img_edge, np.ones((2, 2), dtype=np.int8))
# inceltme
img_edge_erode = cv2.erode(img_edge_dilate, np.ones((2, 2), dtype=np.int8))

cv2.imshow('resized_img', resized_img)
cv2.imshow('img_edge', img_edge)
cv2.imshow('img_edge_dilate', img_edge_dilate)
cv2.imshow('img_edge_erode', img_edge_erode)

cv2.waitKey(0)
