import cv2
import math
import time
from ultralytics import YOLO
from sort import *

model = YOLO('yolov8l.pt')

mask = cv2.imread('videos/mask.png')

# reading the image
capture = cv2.VideoCapture('videos/cars.mp4')

tracker = Sort(max_age=20, min_hits=3, iou_threshold=0.3)

capture.set(3,1280)
capture.set(4,720)

prev_frame_time = 0
new_frame_time = 0

LINE = [300,300,750,300]

totalCount=[]

while True:
    new_frame_time = time.time() # start timing

    isTrue, frame = capture.read()

    imgRegion = cv2.bitwise_and(frame,mask)

    results = model(imgRegion, stream=True)

    detections = np.empty((0,5))
    for r in results:
        boxes = r.boxes
        for bbox in boxes:
            x1,y1,x2,y2 = bbox.xyxy[0]
            x1,y1,x2,y2 = int(x1), int(y1), int(x2), int(y2)

            cls=int(bbox.cls[0])

            conf = math.ceil(bbox.conf[0]*100)/100

            currentClass = model.names[cls]
            if currentClass == 'car' or currentClass == 'bus'\
                or currentClass == 'truck'  or currentClass == 'motorcycle' and conf>0.1:
                cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,255),3)
                cv2.putText(frame,f'{currentClass} {conf}',(x1,y1-5),cv2.FONT_HERSHEY_PLAIN,1,(0,255,0),1)

                currentArray = np.array([x1,y1,x2,y2,conf])
                detections = np.vstack((detections,currentArray))

    # resultsTracker = tracker.update(detections)

    # for result in resultsTracker:
    #     x1,y1,x2,y2,id = result
    #     x1,y1,x2,y2 = int(x1), int(y1), int(x2), int(y2)
    #     cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,255),3)
    #     cv2.putText(frame,f'{int(id)}',(x1,y1-5),cv2.FONT_HERSHEY_PLAIN,1,(0,255,0),2)

    #     w,h = x2-x1,y2-y1
    #     cx = x1 + w//2
    #     cy = y1 + h//2
    #     cv2.circle(frame, (cx,cy), radius=5, color = (255,255,0), thickness=(cv2.FILLED))

    #     if  LINE[0]<cx<LINE[2] and LINE[1]<cy<LINE[1]+20:
    #         if totalCount.count(id)==0: 
    #             totalCount.append(id)

    totalCars = len(totalCount)

    fps = 1/ (new_frame_time - prev_frame_time)
    fps = round(fps,2)
    prev_frame_time = new_frame_time

    cv2.line(frame,(LINE[0],LINE[1]),(LINE[2],LINE[3]), [0,0,255], 5)
    cv2.putText(frame,f'FPS: {fps} Total Vehicles: {totalCars}',(10,30),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)

    cv2.imshow('detection', frame)

    cv2.waitKey(1)


capture.release()

cv2.destroyAllWindows()



# cv2.waitKey(0)