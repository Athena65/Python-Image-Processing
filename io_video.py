import os
import cv2

# read video
video_path = os.path.join('.', 'data', 'doggie.mp4')

video = cv2.VideoCapture(video_path)  # read video

# visualize proccess

ret = True

while ret:
    ret, frame = video.read()
    # frame oldugu surerce okunmasi icin ret true olmasi gerekir.
    # frame bitince ret flase olacak ve veideo kapanacak
    if ret:  # onemli
        cv2.imshow('frame', frame)
        cv2.waitKey(40)  # 1/25(fps) - 0.04 saniye 40 milisaniy
video.release() # hafizayi serbest birakir
cv2.destroyAllWindows()

