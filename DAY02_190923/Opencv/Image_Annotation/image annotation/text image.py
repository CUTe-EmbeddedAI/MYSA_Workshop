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

imageText = image.copy()
text = "Apollo 11 Saturn V Launch, July 16, 1969"
fontScale = 2.3
fontFace = cv2.FONT_HERSHEY_PLAIN
fontColor = (0, 255, 0)
fontThickness = 2

cv2.putText(imageText, text, (200, 700), fontFace, fontScale, fontColor, fontThickness, cv2.LINE_AA);

# Display the image
plt.imshow(imageText[:,:,::-1])
