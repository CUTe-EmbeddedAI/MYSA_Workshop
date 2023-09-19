# Import the OpenCV library and alias it as 'cv' for easier use.
import cv2 as cv

# Load an image from the file '12.jpg'.
img = cv.imread('12.jpg')

# Display the original image in a window titled 'normal'.
cv.imshow('normal', img)

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

# Call the 'rescaleFrame' function to resize the 'img' using the default scale of 0.75.
resized_image = rescaleFrame(img)

# Display the resized image in a window titled 'resized_image'.
cv.imshow('resized_image', resized_image)

# Wait indefinitely for a key press event. This keeps the image window open until a key is pressed.
cv.waitKey(0)

# After a key is pressed, the window will close, and the program will terminate.
