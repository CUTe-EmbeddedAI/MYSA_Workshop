# Import the OpenCV library.
import cv2
# Create CascadeClassifiers for face and eye detection using pre-trained XML files.
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
# Open a video file for processing. Replace 'test1.mov' with the path to your video file.
cap = cv2.VideoCapture('test1.mov')
while cap.isOpened():
    # Read a frame from the video stream.
    _, img = cap.read()
    # Convert the frame to grayscale for face detection.
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect faces in the grayscale frame using the face_cascade.
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
    # Iterate over the detected faces.
    for (x, y, w, h) in faces:
        # Draw a rectangle around the detected face.
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)
        # Extract the region of interest (ROI) within the detected face for eye detection.
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        # Detect eyes within the ROI using the eye_cascade.
        eyes = eye_cascade.detectMultiScale(roi_gray)
        # Iterate over the detected eyes.
        for (ex, ey, ew, eh) in eyes:
            # Draw a rectangle around the detected eye.
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5)

    # Display the frame with detected faces and eyes.
    cv2.imshow('img', img)

    # Check for the 'q' key press to exit the loop and close the video.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Release the video capture object.
cap.release()

# Close all OpenCV windows.
cv2.destroyAllWindows()
