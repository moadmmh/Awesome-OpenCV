import cv2
import numpy as np

video =cv2.VideoCapture("road_car_view.mp4")

while True:
    ret,or_frame=video.read()
    if not ret :
        video =cv2.VideoCapture("road_car_view.mp4")
        continue
    frame=cv2.GaussianBlur(or_frame,(5,5),0)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    lower_y=np.array([18,94,140])
    upper_y=np.array([48,255,255])
    
    mask=cv2.inRange(hsv,lower_y,upper_y)
    edges=cv2.Canny(mask,74,150)
    lines=cv2.HoughLinesP(edges,1,np.pi/180,50,maxLineGap=50)
    if lines is not None:
        for line in lines:
            x1,y1,x2,y2 = line[0]
            cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),5)
    
    cv2.imshow("frame",frame)
    cv2.imshow("edges",edges)
    key=cv2.waitKey(25)
    if(key==27):
        break
    


video.release()
cv2.destroyAllWindows()
