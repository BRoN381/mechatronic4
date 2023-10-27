#import opencv and numpy
import cv2
import numpy as np

#trackbar callback fucntion to update HSV value
def callback(x):
    global H_low,H_high,S_low,S_high,V_low,V_high
    #assign trackbar position value to H,S,V High and low variable
    H_low = cv2.getTrackbarPos('low H','controls')
    H_high = cv2.getTrackbarPos('high H','controls')
    S_low = cv2.getTrackbarPos('low S','controls')
    S_high = cv2.getTrackbarPos('high S','controls')
    V_low = cv2.getTrackbarPos('low V','controls')
    V_high = cv2.getTrackbarPos('high V','controls')


#create a seperate window named 'controls' for trackbar
cv2.namedWindow('controls',2)
cv2.resizeWindow("controls", 550,10);


#global variable
H_low = 0
H_high = 179
S_low= 0
S_high = 255
V_low= 0
V_high = 255

#create trackbars for high,low H,S,V 
cv2.createTrackbar('low H','controls',0,179,callback)
cv2.createTrackbar('high H','controls',179,179,callback)

cv2.createTrackbar('low S','controls',0,255,callback)
cv2.createTrackbar('high S','controls',255,255,callback)

cv2.createTrackbar('low V','controls',0,255,callback)
cv2.createTrackbar('high V','controls',255,255,callback)

cap = cv2.VideoCapture(0)

while(1):
    #read source image
    ret, frame = cap.read()
    # frame = cv2.flip(frame, -1)
    #convert sourece image to HSC color mode
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #
    hsv_low = np.array([H_low, S_low, V_low], np.uint8)
    hsv_high = np.array([H_high, S_high, V_high], np.uint8)

    #making mask for hsv range
    mask = cv2.inRange(hsv, hsv_low, hsv_high)
    numList = [H_low, S_low, V_low, H_high, S_high, V_high]
    for i in range(6):
        numList[i] = str(numList[i])
        numList[i] = ' '*(3-len(numList[i]))+numList[i]
    print (numList[0]+','+numList[1]+','+numList[2]+'\n'+numList[3]+','+numList[4]+','+numList[5])
    print("----------------------------")
    #masking HSV value selected color becomes black
    res = cv2.bitwise_and(frame, frame, mask=mask)

    #show image
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    hor = np.vstack((res, mask))
    hor = cv2.resize(hor, (427,640))
    cv2.imshow('tracking',hor)
    
    #waitfor the user to press escape and break the while loop 
    if cv2.waitKey(1) == ord('q'):
            break
        
#destroys all window
cv2.destroyAllWindows()
