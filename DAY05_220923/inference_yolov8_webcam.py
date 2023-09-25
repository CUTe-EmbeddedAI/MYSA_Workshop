import cv2
from ultralytics import YOLO
import cvzone
import math
import time

cap = cv2.VideoCapture(0)

# set the width and height of the frame
cap.set(3,1280)
cap.set(4,720)

model = YOLO("yolov8n.pt")

prev_frame_time = 0
new_frame_time = 0

while True:
    new_frame_time = time.time()
    success, img = cap.read()
    results = model(img, stream = True) # stream will generate a generator which is more efficient

    for r in results:
        boxes = r.boxes
        for box in boxes:
            # bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            # x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            # cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,255),3) #img,bbox coordinates, color, thickness
            w, h = x2-x1, y2-y1
            bbox = int(x1), int(y1), int(w), int(h)
            cvzone.cornerRect(img,bbox)

            # confidence, round up into 2 decimal places
            conf = math.ceil((box.conf[0] * 100)) / 100
        
            # class name
            cls = int(box.cls[0])
            cvzone.putTextRect(img,f'{model.names[cls]}{conf}',(max(0,x1),max(35,y1)), scale=1, thickness=1)


    fps = 1 / (new_frame_time - prev_frame_time)
    fps = round(fps,2)
    prev_frame_time = new_frame_time
    print(fps)

    cvzone.putTextRect(img,f'FPS: {fps}', (1000,50), scale=1, thickness=1)
    cv2.imshow("Image",img)
    cv2.waitKey(1)