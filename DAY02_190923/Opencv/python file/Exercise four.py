# Import the OpenCV library and alias it as 'cv' for easier use.
import cv2 as cv

# Define a function called 'rescaleFrame' that takes a 'frame' and an optional 'scale' parameter.
def rescaleFrame(frame, scale=0.75):
    # Calculate the new dimensions for the frame based on the specified 'scale'.
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    # Resize the frame using the calculated dimensions and specify the interpolation method as 'cv.INTER_AREA'.
    resized_frame = cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

    # Return the resized frame.
    return resized_frame

# Create a VideoCapture object to capture video frames from 'video.mp4'.
capture = cv.VideoCapture('video.mp4')

# Create an infinite loop to continuously read and display video frames.
while True:
    # Read the next frame from the video capture.
    # 'isTrue' will be True if a frame was successfully read, and 'frame' will contain the frame data.
    isTrue, frame = capture.read()

    # Resize the frame using the 'rescaleFrame' function.
    frame_resized = rescaleFrame(frame)

    # Display the original frame in a window titled 'video1'.
    cv.imshow('video1', frame)

    # Display the resized frame in a window titled 'video resized'.
    cv.imshow('video resized', frame_resized)

    # Wait for a key press event for 20 milliseconds and check if the pressed key is 'd'.
    # If the 'd' key is pressed, break out of the loop and exit.
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

# Release the video capture object to free up resources.
capture.release()

# Close all OpenCV windows.
cv.destroyAllWindows()
