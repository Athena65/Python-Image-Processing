import os
import cv2

img = cv2.imread(os.path.join('.', 'data/whiteboard.jpg'))

# boyut - parametrelerde zıt taraflarda
print(img.shape)

# line - cizgi (x , y ) (x, y) , BGR , thickness
cv2.line(img, (100, 150), (300, 450), (0, 255, 0), 3)

# rectangle - dikdortgen (sol ust x, sol ust  y), (sag alt x, sag alt y), BGR, thickness
cv2.rectangle(img, (100, 250), (350, 500), (0, 0, 255), 10)

# circle - cember (cemberin ortasi x, cemberin ortasi y) , yaricap
cv2.circle(img, (400, 300), 150, (255, 0, 0), 6)

# text - yazi (x,y) , font , yazi araligi, renk, kalinlik
cv2.putText(img, 'Hey yo, how are you?', (500, 500), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 7)

cv2.imshow('img', img)
cv2.waitKey(0)


