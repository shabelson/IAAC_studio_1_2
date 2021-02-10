
#!/usr/bin/env python3


import cv2  # OpenCV library
import numpy as np  # Numpu library
import argparse
import sys
import os
dirPath = "C:\\Users\\shabe\\OneDrive\\Documents\\GitHub\\IAAC_studio_1_2\\industria\\balcon1"
files = os.listdir(dirPath)
#print (files)
newfoler = dirPath+"\\masked"
try:
    flies = os.mkdir(newfoler)
except:
    pass
files = [files[0]]
for i,file in enumerate(files):
    fname = dirPath+'\\'+file 
    newFname = newfoler+'\\'+file 
    image = cv2.imread(fname)
    #print(type(image))
    # if image is loaded
    if image is not None:
        scale_percent = 65  # percent of original size
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
        resizedArea = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
        
        gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
        
        ret, thresh = cv2.threshold(gray, 120, 255, 0)
    
        
        kernel = np.ones((9, 9), np.uint8)
        dst = np.ones(dim)

        
        dst=cv2.bitwise_not(thresh)
            
        img_erosion = cv2.erode(thresh, kernel, iterations=1)

        blurred = cv2.GaussianBlur(img_erosion, (11, 11), cv2.BORDER_DEFAULT)
        blurred = cv2.bitwise_not(blurred)
        maskRGB = cv2.cvtColor(blurred,cv2.COLOR_BAYER_GR2RGB_EA)
        print (file)
    
        masked = cv2.bitwise_and(resized ,maskRGB)
        

cv2.imshow("n",masked)
cv2.waitKey(0)
        #cv2.imwrite(newFname,masked)
"""
    contours,hierarchy = cv2.findContours(blurred, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #a, contours, hierarchy 
    #.imshow("Blurred", blurred)

    final_contours = []
    for index, cnt in enumerate(contours):
        if hierarchy[0][index][2] == -1:

            if cv2.contourArea(cnt) > 2000:
                final_contours.append(cnt)

    coordinates = []
    for cnt in final_contours:
        coordinates.append(np.squeeze(cnt, axis=(1,)))

    boundaries = []
    for cnt in coordinates:
        boundaries.append(cv2.approxPolyDP(cnt, 7, True))

    for crv in boundaries:
        cv2.drawContours(resized, [crv], 0, (0, 0, 255), 3)
        cv2.drawContours(resizedArea, [crv], 0, (200, 200, 200), 2)
    #cv2.imshow('Contours', resized)
    cv2.waitKey(0)

    color_msg = ''
    for ind, c in enumerate(contours):
        M = cv2.moments(c)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        pass#(resized[cY, cX])
        #print(resized.shape)

        (b, g, r) = image[int(cY), int(cX)]
        #print(b, g, r)
        colortext = str(b) + "," + str(g) + "," + str(r)

        font = cv2.FONT_HERSHEY_SIMPLEX

        org = (cX, cY)

        fontScale = .4

        color = (0, 0, 255)

        thickness = 2
        cv2.putText(resized, colortext, (cX, cY), font,
                    fontScale, color, thickness, cv2.LINE_AA, False)
        color_msg += colortext + ';'

    cv2.drawContours(resized, [crv], 0, (0, 0, 255), 3)
    cv2.drawContours(resizedArea, [crv], 0, (200, 200, 200), 2)
    cv2.circle(resized, (cX, cY), 7, (217, 23, 23), -1)

    area = cv2.contourArea(contours[True])

    cv2.drawContours(resized, [crv], 0, (0, 0, 255), 3)
    cv2.drawContours(resizedArea, [crv], 0, (200, 200, 200), 2)
    cv2.putText(resized, "#{}".format(ind), (cX - 20, cY + 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 252, 252), 2)
    cv2.putText(resizedArea, "#{}".format(
        area), (cX - 20, cY + 80), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 252, 252), 2)


    #cv2.imshow('Area', resizedArea)
    final_msg = ''
    for boundary in boundaries:
        simplified = np.squeeze(boundary, axis=(1))
        crds_list = simplified.tolist()
        str_list = []
        for i in simplified:
            x = i[0]
            y = i[1]
            str_list.append(str(x)+','+str(y))
        msg = '+'.join([str(elem) for elem in str_list])
        final_msg += msg + ';'
"""