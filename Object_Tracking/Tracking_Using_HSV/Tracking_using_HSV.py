import cv2
import numpy as np
def nothing(x):
    pass

cv2.namedWindow("Trackbars")

cv2.createTrackbar("L-H","Trackbars",0,179,nothing)
cv2.createTrackbar("L-S","Trackbars",0,255,nothing)
cv2.createTrackbar("L-V","Trackbars",0,255,nothing)
cv2.createTrackbar("U-H","Trackbars",179,179,nothing)
cv2.createTrackbar("U-S","Trackbars",255,255,nothing)
cv2.createTrackbar("U-V","Trackbars",255,255,nothing)
cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    ret, frame = cap.read()
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h= cv2.getTrackbarPos("L-H,","Trackbars")
    l_s= cv2.getTrackbarPos("L-S,","Trackbars")
    l_v= cv2.getTrackbarPos("L-V,","Trackbars")
    u_h= cv2.getTrackbarPos("U-H,","Trackbars")
    u_s= cv2.getTrackbarPos("U-S,","Trackbars")
    u_v= cv2.getTrackbarPos("U-V,","Trackbars")


    lower_blue = np.array([l_h,l_s,l_v])
    upper_blue = np.array([u_h,u_s,u_v])
    
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    #cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
