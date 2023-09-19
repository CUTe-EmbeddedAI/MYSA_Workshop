# Import the OpenCV library and alias it as 'cv' for easier use.
import cv2 as cv
import numpy as np

# Load an image from the file '12.jpg'.
img = cv.imread('12.jpg')

# Display the original image in a window titled 'normal'.
cv.imshow('normal', img)

# Define a function called 'rotate' that takes an 'img' (image), 'angle' (rotation angle in degrees),
# and an optional 'rotPoint' parameter (the point around which the image will be rotated, defaults to the center).
def rotate(img, angle, rotPoint=None):
    # Get the height and width of the image.
    (height, width) = img.shape[:2]

    # If 'rotPoint' is not specified, use the center of the image as the rotation point.
    if rotPoint is None:
        rotPoint = (width // 2, height // 2)

    # Create a rotation matrix ('rotMat') using 'cv.getRotationMatrix2D'.
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)

    # Define the dimensions for the output (rotated) image.
    dimensions = (width, height)

    # Apply the rotation transformation to the image using 'cv.warpAffine'.
    rotated_img = cv.warpAffine(img, rotMat, dimensions)

    # Return the rotated image.
    return rotated_img

# Call the 'rotate' function to rotate the 'img' by 45 degrees.
rotated = rotate(img, 45)

# Display the rotated image in a window titled 'rotated_image'.
cv.imshow('rotated_image', rotated)

# Wait indefinitely for a key press event. This keeps the image window open until a key is pressed.
cv.waitKey(0)

# After a key is pressed, the window will close, and the program will terminate.
