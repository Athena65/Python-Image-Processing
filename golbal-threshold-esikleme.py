import os
import cv2
# image to binary image(siyah, beyaz)
# threshold = eşik
# parcalara ayirma icin
# objec tespiti icin kullanilabilir .
img = cv2.imread(os.path.join('.', 'data/bear.jpg'))
resized_img = cv2.resize(img, (480, 320))

gray_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray_img, 80, 255, cv2.THRESH_BINARY)
# img blurlaniyor noise siliniyor.
thresh = cv2.blur(thresh, (10, 10))

ret, thresh = cv2.threshold(thresh, 80, 255, cv2.THRESH_BINARY)


cv2.imshow('gray_img', gray_img)
cv2.imshow('thresh', thresh)
cv2.waitKey(0)
