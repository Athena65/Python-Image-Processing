import os
import cv2
# noise(gürültü) eklemek için
img = cv2.imread(os.path.join('.', 'data/fereelancer.png'))
img2 = cv2.imread(os.path.join('.', 'data/Highimgnoise.jpg'))

resized_img = cv2.resize(img, (480, 320))
resized_img2 = cv2.resize(img2, (480, 320))
# blur derecesi
k_size = 7

# blured_img = cv2.blur(resized_img, (k_size, k_size))
blured_img2 = cv2.blur(resized_img2, (k_size, k_size))
# gaussian_blur_img2 = cv2.GaussianBlur(resized_img, (k_size, k_size), 5)
gaussian_blur_img2 = cv2.GaussianBlur(resized_img2, (k_size, k_size), 5)
# median_blur_img = cv2.medianBlur(resized_img, k_size)
median_blur_img2 = cv2.medianBlur(resized_img2, k_size)


cv2.imshow('resized_img2', resized_img2)
# cv2.imshow('resized_img', resized_img)
cv2.imshow('gaussian_blur_img', gaussian_blur_img2)
# cv2.imshow('gaussian_blur_img', gaussian_blur_img)
cv2.imshow('median_blur_img', median_blur_img2)
# cv2.imshow('median_blur_img', median_blur_img)
cv2.imshow('blured_img', blured_img2)
# cv2.imshow('blured_img', blured_img)
cv2.waitKey(0)
