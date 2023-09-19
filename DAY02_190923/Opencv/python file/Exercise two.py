# Import the OpenCV library and alias it as 'cv' for easier use.
import cv2 as cv

# Create a VideoCapture object, which is used to capture video frames from a file.
# In this case, it opens and reads frames from 'video.mp4'.
capture = cv.VideoCapture('video.mp4')

# Create an infinite loop to continuously read and display video frames.
while True:
    # Read the next frame from the video capture.
    # 'isTrue' will be True if a frame was successfully read, and 'frame' will contain the frame data.
    isTrue, frame = capture.read()

    # Display the current frame in a window titled 'video1'.
    cv.imshow('video1', frame)

    # Wait for a key press event for 20 milliseconds and check if the pressed key is 'd'.
    # If the 'd' key is pressed, break out of the loop and exit.
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

# Release the video capture object to free up resources.
capture.release()

# Close all OpenCV windows.
cv.destroyAllWindows()
