import cv2
import math
import time
from ultralytics import YOLO

model = YOLO('yolov8n.pt')

# reading the image
capture = cv2.VideoCapture(0)

# capture.set(3,1280)
# capture.set(4,720)

prev_frame_time = 0
new_frame_time = 0

while True:
    new_frame_time = time.time() # start timing

    isTrue, frame = capture.read()

    results = model(frame, stream=True)
    
    for r in results:
        boxes = r.boxes
        for bbox in boxes:
            print(len(bbox.cls))
            x1,y1,x2,y2 = bbox.xyxy[0]
            x1,y1,x2,y2 = int(x1), int(y1), int(x2), int(y2)

            cls_idx=int(bbox.cls[0])
            cls_names= model.names[cls_idx]

            conf = round(float(bbox.conf[0]), 2)
            # conf = bbox.conf[0]

            cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,255),4)
            cv2.putText(frame,f'{cls_names} {conf}',(x1,y1-5),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)


    fps = 1/ (new_frame_time - prev_frame_time)
    fps = round(fps,2)
    prev_frame_time = new_frame_time

    cv2.putText(frame,f'FPS: {fps}',(10,30),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)

    cv2.imshow('detection', frame)

    cv2.waitKey(1)
    

capture.release()

cv2.destroyAllWindows()
