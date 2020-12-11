
## color+opacity
"""""""""""""""
##### color+opacity
'import cv2

image1 = cv2.imread('MCQPaper.jpg')
image = cv2.resize(image1, (500,500), interpolation=cv2.INTER_LINEAR)
overlay = image.copy()

x, y, w, h = 100, 100, 100, 100  # Rectangle parameters
cv2.rectangle(overlay, (x, y), (x+w, y+h), (0, 200, 0), -1)  # A filled rectangle

alpha = 1  # Transparency factor.

# Following line overlays transparent rectangle over the image
image_new = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)
cv2.imshow("test",image_new)
cv2.waitKey(0) """
#

## Mask a logo
""""## Mask a logo
# Load two images
img1 = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv_logo.png')

# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]

# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst

cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
"""

"""


##IP camera Indian guy
""" 
import numpy as np
import cv2
address="http://192.168.1.229:4747" # Phone IP Addresss
cap = cv2.VideoCapture(address)

#cap.open()

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
"""
#

## IP camera cv2 forum
"""
import numpy as np
import cv2
address="http://192.168.1.229:4747/video" # Phone IP Addresss
cv2.namedWindow("win")

camera = cv2.VideoCapture(0)
camera.open(address)


print("acess")

while True:
    print('access1')
    ok, image = camera.read()
    print("image",image)
    if not ok:
        print( 'no image read')
        break
    cv2.imshow("win", image)
    k = cv2.waitKey(1) & 0xff
    if k == 27 : break # Esc pressed
"""