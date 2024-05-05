import cv2

# read webcam
webcam = cv2.VideoCapture(0)  # bagli baska webcam yoksa 0 dir varsa 2 veya id si neyse o olur.

# visualize webcam

while webcam.isOpened(): # true cunku son yok o yuzden sonsuz dongu
    ret, frame = webcam.read()

    cv2.imshow('frame', frame)
    if cv2.waitKey(40) & 0xFF == ord('q'): # kullanici q'ya basarsa windowu kapatir
        break

# 1/25


webcam.release()
cv2.destroyAllWindows()
