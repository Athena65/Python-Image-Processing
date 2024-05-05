import os
import cv2
#adaptive simple dan daha iyi

img = cv2.imread(os.path.join('.', 'data/handwritten.jpg'))
# resized_img = cv2.resize(img, (480, 320))

# kendi ayarliyor sayilari(255den sonra bisey girmeye gerek yok) . 255 den buyuk olanlari kendi buluyor
# 20, 30 degistirilir uygunu secilir

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

adaptive_thresh = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 30)
ret, simple_thresh = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)

cv2.imshow('img', img)
cv2.imshow('adaptive_thresh', adaptive_thresh)
cv2.imshow('simple_thresh', simple_thresh)
cv2.waitKey(0)
