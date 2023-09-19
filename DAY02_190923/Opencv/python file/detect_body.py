# Import the necessary libraries
import cv2
from cvzone.PoseModule import PoseDetector

# Create a PoseDetector object
detector = PoseDetector()

# Open a video file for reading
cap = cv2.VideoCapture('test.mp4')

# Start an infinite loop to process frames from the video
while True:
   # Read the next frame from the video
   success, img = cap.read()
   
   # Use the PoseDetector to find the pose in the current frame
   img = detector.findPose(img)
   
   # Use the PoseDetector to find the positions of landmarks and bounding box information
   lmList, bboxInfo = detector.findPosition(img, bboxWithHands=True)
   
   # Display the resulting frame with the pose and landmarks
   cv2.imshow("result", img)
   
   # Check if the 'd' key is pressed (for quitting the loop)
   if cv2.waitKey(20) & 0xFF == ord('d'):
        break

# Release the video capture object
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
