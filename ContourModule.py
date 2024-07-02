"""
Contour Module 
Finds the Contours in an image. 

"""

import cv2
import numpy as np 


def preProcessing(img, blur= 5, cannyThres=[50,50],dia = 1):

    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(blur,blur),1)
    imgCanny = cv2.Canny(imgBlur,cannyThres[0],cannyThres[1])
    kernel = np.ones((5,5), np.uint8)
    imgDia = cv2.dilate(imgCanny, kernel, iterations =dia)
    return imgDia


def findContours(img, imgPre, minArea=1000, sort= True, filter= 0,drawCon=True ):

    conFound = []
    imgContours = img.copy()
    contours, hierarchy = cv2.findContours(imgPre,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for cnt in contours: 
        area = cv2.contourArea(cnt)
        if area>minArea:
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            #print(len(approx))
            if len(approx) == filter or filter == 0:
                if drawCon:cv2.drawContours(imgContours,cnt,-1, (255,0,255), 3)
                x, y, w, h = cv2.boundingRect(approx)
                cv2.rectangle(imgContours, (x,y), (x+w,y+h), (0,255,0),2)
                cv2.circle(imgContours, (x+(w//2),y+(h//2)),5, (0,255,0), cv2.FILLED)
                conFound.append([cnt,area,[x,y,w,h]])
    
    if sort: 
        conFound = sorted(conFound, key = lambda x:x[1], reverse = True)

    return imgContours, conFound



def main ():
    img = cv2.imread("../Resources/shapes.png")
    imgPre = preProcessing(img)
    imgContours, conFound = findContours(img, imgPre)
    cv2.imshow("Image",img)
    cv2.imshow("Image Preprocessed",imgPre)
    cv2.imshow("Image Contours",imgContours)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()















