import os
import cv2

# read image
image_path = os.path.join('data', 'data', 'punisher.jpg')

# **
img = cv2.imread(image_path)

# write image

cv2.imwrite(os.path.join('data', 'data', 'punisher_out.jpg'), img) # copy paste islemi ayni resim

# visualize image

cv2.imshow('image', img)  # resmi gosteriyor
cv2.waitKey(0)  # wait until I press a key bu olmazsa calismaz aninda kapanir pencere
# cv2.waitKey(5000) # 5 saniye bekler
