# Import the OpenCV library and alias it as 'cv' for easier use.
import cv2 as cv

# Load an image from the file 'image.jpg' located in the 'photos' directory.
# The 'imread' function reads an image and stores it in the 'img' variable.
img = cv.imread('photos/image.jpg')

# Display the loaded image in a window with the title 'photo'.
# The 'imshow' function is used for this purpose.
cv.imshow('photo', img)

# Wait indefinitely for a key press event. This keeps the image window open
# until a key is pressed. The argument '0' means that it will wait forever.
cv.waitKey(0)

# After a key is pressed, the window will close, and the program will terminate.

