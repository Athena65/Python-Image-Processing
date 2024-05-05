import os
import cv2


img = cv2.imread(os.path.join('.', 'data/dogs.jpg'))

# resizing
resized_img = cv2.resize(img, (480, 320))  # width, height

print(img.shape)  # (height , width)
print(resized_img.shape)

cv2.imshow('img', img)
cv2.imshow('resized_img', resized_img)
cv2.waitKey(0)
