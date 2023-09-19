# Import libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image 
%matplotlib inline
import matplotlib
matplotlib.rcParams['figure.figsize'] = (9.0, 9.0)
from IPython.display import Image

#mount google drive to colab environment
from google.colab import drive
drive.mount('/content/gdrive')

#path of example directory (use download cloned directory from day1)
path = "/content/gdrive/MyDrive/DLIVACV_workshop/day1/opencv/03_Image_Annotation/"


# Read in an image
image = cv2.imread(path+"Apollo_11_Launch.jpg", cv2.IMREAD_COLOR)

# Draw a rectangle (thickness is a positive integer)
imageRectangle = image.copy()

cv2.rectangle(imageRectangle, (500, 100), (700,600), (255, 0, 255), thickness=5, lineType=cv2.LINE_8);

# Display the image
plt.imshow(imageRectangle[:,:,::-1])
