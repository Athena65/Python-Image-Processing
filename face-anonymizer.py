import os

import cv2
import mediapipe as mp
# blur a face and output blurred image to ./output dir

output_dir = './output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# read image

img_path = './data/testimage.jpg'
img = cv2.imread(img_path)

H, W, _ = img.shape

# detect faces

mp_face_detection = mp.solutions.face_detection
# model_selection=0 yuzler kameraya yakinsa(2 metre) model_selection=1 (5 metre) yuzler kameraya uzaksa
with mp_face_detection.FaceDetection(min_detection_confidence=0.5, model_selection=0) as face_detection:
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    out = face_detection.process(img_rgb)

    if out.detections is not None: # if it finds a human face
        for detection in out.detections:
            location_data = detection.location_data
            bbox = location_data.relative_bounding_box

            x1, y1, w, h = bbox.xmin, bbox.ymin, bbox.width, bbox.height

            x1 = int(x1 * W)
            y1 = int(y1 * H)
            w = int(w * W)
            h = int(h * H)

            # cv2.rectangle(img, (x1, y1), (x1 + w, y1 + h), (255, 0, 0))
            # blur faces

            img[y1: y1 + h, x1: x1 + w, :] = cv2.blur(img[y1: y1 + h, x1: x1 + w, :], (50, 50))


#  cv2.imshow('img', img)
#  cv2.waitKey(0)

#  save image
cv2.imwrite(os.path.join(output_dir, 'blurred_img.jpg'), img)
