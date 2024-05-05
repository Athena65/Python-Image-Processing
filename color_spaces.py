import os

import cv2

img = cv2.imread(os.path.join('.', 'data/bird.jpg'))

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# 3 channel to 1 channel
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# renk belirlemede
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

resized_img = cv2.resize(img, (480, 320))
resized_img_rgb = cv2.resize(img_rgb, (480, 320))
resized_img_gray = cv2.resize(img_gray, (480, 320))
resized_img_hsv = cv2.resize(img_hsv, (480, 320))


cv2.imshow('resized_img', resized_img)
cv2.imshow('resized_img_rgb', resized_img_rgb)
cv2.imshow('resized_img_gray', resized_img_gray)
cv2.imshow('resized_img_hsv', resized_img_hsv)


cv2.waitKey(0)
