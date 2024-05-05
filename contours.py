import os
import cv2
# object tespiti ****
# goruntuler siyah beyaz olmali
img = cv2.imread(os.path.join('.', 'data/birds.jpg'))
img2 = cv2.imread(os.path.join('.', 'data/birds.jpg'))

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)
# inv background siyah objeler beyaz

# kontur : her ayrik obje icin sinirlarini belirleyen bir cizgi var
# her beyaz obje eger ayrik ise onlarin sinirlari ayridir
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# area of a contour : bolgelerini degerleri
# contour degerleri buyuk olanlari yani alanlari buyuk olanlari alacagiz
# kucukleri gormezden geleceggiz
# noise yani gurultuyu azaltmak icin
for cnt in contours:
    if cv2.contourArea(cnt) > 20:
        # cv2.drawContours(img, cnt, -1, (0, 255, 0), 1) # bolgeleri cizme
        # object tespiti ****
        x1, y1, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(img, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 1)

cv2.imshow('img2', img2)
cv2.imshow('img', img)
cv2.imshow('thresh', thresh)
cv2.waitKey(0)
