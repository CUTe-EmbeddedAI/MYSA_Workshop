import cv2

# reading the image
img = cv2.imread('images/gambar1.jpg')
masker = cv2.imread('images/mask.png',0)

# apply the mask
masked_img = cv2.bitwise_and(img,img,mask = masker)

# showing the image
cv2.imshow('gambar saya',img)
cv2.imshow('masked image',masked_img)

cv2.waitKey(0)