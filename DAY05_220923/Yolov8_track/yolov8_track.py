import cv2
import numpy as np
from ultralytics import YOLO
from collections import defaultdict

# Load the YOLOv8 model
model = YOLO('yolov8n.pt')

# Open the video file
cap = cv2.VideoCapture('videos/cars.mp4')

# Store the track history
track_history = defaultdict(lambda: [])

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, img = cap.read()

    # Run YOLOv8 tracking on the frame, persisting tracks between frames
    results = model.track(img, persist=True, show=True, tracker="bytetrack.yaml")

    # Get the boxes and track IDs
    boxes = results[0].boxes.xywh.cpu()
    track_ids = results[0].boxes.id.int().cpu().tolist()

    # Visualize the results on the frame
    annotated_frame = results[0].plot()

    # Plot the tracks
    for box, track_id in zip(boxes, track_ids):
        x, y, w, h = box
        track = track_history[track_id]
        track.append((float(x), float(y)))  # x, y center point
        if len(track) > 90:  # retain 90 tracks for 90 frames
            track.pop(0)

    # Draw the tracking lines
    points = np.hstack(track).astype(np.int32).reshape((-1, 1, 2))
    cv2.polylines(annotated_frame, [points], isClosed=False, color=(230, 230, 230), thickness=10)


    cv2.imshow("Image",annotated_frame)
    cv2.waitKey(1)