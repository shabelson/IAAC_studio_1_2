import cv2
import numpy as np

path = 'test_01.PNG'
img=cv2.imread(path)


def getContours(img):
    contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area=cv2.contourArea(cnt)
        print(area)
        if area>5:
            cv2.drawContours(imgCoutour,cnt,-1,(0,0,255),1)
            peri=cv2.arcLength(cnt,True)
            #print(peri)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)
            #print(approx)
            print(len(approx))
            objCor=len(approx)
            x,y,w,h=cv2.boundingRect(approx)
            cv2.rectangle(imgCoutour, (x, y), (x + w, y + h), (0, 255, 0), 2)


            if objCor==4: objectType="Windows"
            else:objectType="None"
            cv2.putText(imgCoutour,objectType,(x+(w//2)-10,y+(h//2)-10),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL,0.7,(0,0,255),1)




path = 'test_01.PNG'
img=cv2.imread(path)
imgCoutour=img.copy()

#In order to extract the shape, we need to Gray and Blur the image.

imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny=cv2.Canny(imgBlur,150,150)
getContours(imgCanny)


#cv2.imshow("Original",img)
#cv2.imshow("Gray",imgGray)
#cv2.imshow("Blur",imgBlur)
cv2.imshow("Canny",imgCanny)
cv2.imshow("Coutour",imgCoutour)
cv2.waitKey(0)