import os
import cv2

img = cv2.imread(os.path.join('.', 'data/dogs.jpg'))

print(img.shape)

# crop islemi

cropped_imaged = img[40:605, 338:710]  # height width
cv2.imshow('img', img)
cv2.imshow('cropped_imaged', cropped_imaged)
cv2.waitKey(0)
