import cv2

# reading the image
img = cv2.imread('images/gambar1.jpg')

# image = cv2.rectangle(image, start_point, end_point, color, thickness)
# cv2.rectangle(img,(460,60),(740,470),(0,255,255),4)

# cv2.circle(image, center_coordinates, radius, color, thickness)
# cv2.circle(img,(600,300),200, (255,255,0),5)

# cv2.line(image, start_point, end_point, color, thickness) 
# cv2.line(img,(100,100), (600,600),(0,0,255),7)

# image = cv2.putText(image, 'OpenCV', org, font, 
                #    fontScale, color, thickness, cv2.LINE_AA)

myText = 'my name is hasan'
cv2.putText(img,myText,(10,50),cv2.FONT_HERSHEY_PLAIN,5,(255,0,0),2,cv2.LINE_AA)

# showing the image
cv2.imshow('gambar saya',img)

cv2.waitKey(0)

