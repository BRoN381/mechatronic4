import cv2
import numpy as np
cap=cv2.VideoCapture(0)

#==============CHANGE YOUR MASK HERE===============
lower=np.array([  0,192,172])
upper=np.array([  5,255,255])   

def findSign(img):
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,lower,upper)
    result=cv2.bitwise_and(img,img,mask=mask)
    result = cv2.cvtColor(result,cv2.COLOR_BGR2GRAY)
    contours, hierarchy = cv2.findContours(result, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  
    for cnt in contours:
        cv2.drawContours(img, cnt, -1, (0, 255, 0), 3)
        area = cv2.contourArea(cnt)
        if area > 10000:  # look for only lagre signs
            peri = cv2.arcLength(cnt, True)
            vertices = cv2.approxPolyDP(cnt, peri * 0.02, True)
            corners = len(vertices) 
            x, y, w, h = cv2.boundingRect(vertices)
            if corners == 8:  # find circle
                cv2.putText(img, "circle", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                return img
    cv2.putText(img, "None", (10, 480-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    return img    


while True:
    ret, frame = cap.read()  
    if ret:
        imgContour=findSign(frame.copy())
        cv2.imshow("contour", imgContour)
    else:
        break
    if cv2.waitKey(1)==ord("q"):
        break
