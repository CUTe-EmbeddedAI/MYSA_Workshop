# Import the OpenCV library and alias it as 'cv' for easier use.
import cv2 as cv
import numpy as np

# Load an image from the file '12.jpg'.
img = cv.imread('12.jpg')

# Display the original image in a window titled 'normal'.
cv.imshow('normal', img)

# Define a region of interest (ROI) by cropping a portion of the original image.
# Here, we're selecting a rectangular region from (200,300) to (400,400).
# This creates a smaller image called 'cropped'.
cropped = img[200:400, 300:400]

# Display the cropped region in a window titled 'cropped'.
cv.imshow('cropped', cropped)
# Wait indefinitely for a key press event. This keeps the image window open until a key is pressed.
cv.waitKey(0)
