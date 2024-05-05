import cv2
from util import get_limits
from PIL import Image

yellow = [0, 255, 255]  # BGR yellow value

# webcam calistirma
# HSV (hue=renk tonu, saturation=doyma , value=deger)
# sari icin sadece bir deger vermez bir aralik verir araligi belirtmek gerekir
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    # color detection : BGR -> degistirilmeli isleme uygun olarak
    hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color=yellow)

    # bu aralaik util.py'den gelicek :
    # location of all pixels
    mask = cv2.inRange(hsv_img, lowerLimit, upperLimit)
    mask_ = Image.fromarray(mask)  # numpy array pillow 'a cevriliyor

    bbox = mask_.getbbox()  # sinirlayici kutu(pillowdan)

    if bbox is not None:
        x1, y1, x2, y2 = bbox

        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    # sadece mask'de olan renk araligi gosterir
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()  # memory bosaltma

cv2.destroyAllWindows()
