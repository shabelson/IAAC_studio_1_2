import cv2
import pandas as pd
import numpy as np
# load image
img = cv2.imread("C:\\Users\\shabe\\OneDrive\\Documents\\GitHub\\IAAC_studio_1_2\\industria\\balcon1\\129.JPG")
#C:\Users\shabe\OneDrive\Documents\GitHub\IAAC_studio_1_2\industria\balcon1
# add blur because of pixel artefacts 

#cv2.GaussianBlur()
img = cv2.GaussianBlur(img, (1, 1),1)
# convert to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 

cv2.imwrite("C:\\Users\\shabe\\OneDrive\\Documents\\GitHub\\IAAC_studio_1_2\\industria\\balcon1\\129_HSV.JPG",hsv)
cv2.imshow("hsv",hsv)
grey = cv2.cvtColor(hsv,cv2.COLOR_BAYER)
greyHSV = np.asarray(grey,"int32")

df_describe = pd.DataFrame(greyHSV)
df_describe.describe()
# set lower and upper color limits
#15,255,150
lower_val = (0, 200, 150)
upper_val = (30,255,200)
# Threshold the HSV image to get only green colors
#print (max(hsv))
mask = cv2.inRange(hsv, lower_val, upper_val)
cv2.imwrite("C:\\Users\\shabe\\OneDrive\\Documents\\GitHub\\IAAC_studio_1_2\\industria\\balcon1\\129_msk.JPG",mask)
# apply mask to original image
res = cv2.bitwise_and(img,img, mask= mask)
#show imag
cv2.imshow("Result", res)
# detect contours in image
contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# draw filled contour on result
for cnt in contours:
    cv2.drawContours(res, [cnt], 0, (0,0,255), 2)
# detect edges in mask
edges = cv2.Canny(mask,100,100)
# to save an image use cv2.imwrite('filename.png',img)
#show images
#cv2.imshow("d",img)
#cv2.imshow("Result_with_contours", res)
#cv2.imshow("Mask", mask)
#cv2.imshow("Edges", edges)
#
#cv2.destroyAllWindows()
# 
# 


cv2.waitKey(0)