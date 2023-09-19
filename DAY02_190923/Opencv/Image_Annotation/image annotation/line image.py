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

imageLine = image.copy()

# The line starts from (200,100) and ends at (400,100)
# The color of the line is YELLOW (Recall that OpenCV uses BGR format)
# Thickness of line is 5px
# Linetype is cv2.LINE_AA

cv2.line(imageLine, (200, 100), (400, 100), (0, 255, 255), thickness=5, lineType=cv2.LINE_AA);

# Display the image
plt.imshow(imageLine[:,:,::-1])
