import os
import argparse
import cv2
import mediapipe as mp
# blur a face and output blurred image to ./output dir


def process_img(img, face_detection):
    H, W, _ = img.shape

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
        return img


args = argparse.ArgumentParser()
# can be image, video , webcam - change default value for purpose
args.add_argument("--mode", default='webcam')
# read file path - change default value for purposed file
args.add_argument("--filePath", default=None)  # ./data/blury.mp4 #./data/blury.jpg

args = args.parse_args()

output_dir = './output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)



# detect faces

mp_face_detection = mp.solutions.face_detection
# model_selection=0 yuzler kameraya yakinsa(2 metre) model_selection=1 (5 metre) yuzler kameraya uzaksa
with mp_face_detection.FaceDetection(min_detection_confidence=0.5, model_selection=0) as face_detection:

    if args.mode in ["image"]:
        # read image
        img = cv2.imread(args.filePath)

        img = process_img(img, face_detection)

        # save image
        cv2.imwrite(os.path.join(output_dir, 'blurred_img.jpg'), img)

    elif args.mode in ["video"]:

        cap = cv2.VideoCapture(args.filePath)
        ret, frame = cap.read()

        output_video = cv2.VideoWriter(os.path.join(output_dir, 'blurred_video.mp4'),
                                       cv2.VideoWriter.fourcc(*'MP4V'),
                                       25,
                                       (frame.shape[1], frame.shape[0]))
        while ret:
            frame = process_img(frame, face_detection)

            output_video.write(frame)

            ret, frame = cap.read()

        cap.release()
        output_video.release()

    elif args.mode in ["webcam"]:
        cap = cv2.VideoCapture(0)

        ret, frame = cap.read()
        while ret:
            frame = process_img(frame, face_detection)

            cv2.imshow('frame', frame)
            cv2.waitKey(25)

            ret, frame = cap.read()
        # to release memory
        cap.release()




