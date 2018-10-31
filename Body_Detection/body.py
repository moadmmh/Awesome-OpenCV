import cv2
detector=cv2.CascadeClassifier('haarcascade_fullbody.xml')
img = cv2.imread("sample1.jpg",cv2.IMREAD_COLOR)

Id="out_sample"

while(True):
    
    bodyy = detector.detectMultiScale(img, 1.1, 4)
    for (x,y,w,h) in bodyy:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        
        #saving the captured body into directory
        cv2.imwrite(r"\Your Directory\ "+Id +".jpg", img[y:y+h,x:x+w])
        #showing the frame with a rectangle surrounding the body
        cv2.imshow('frame',img)

    #press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cv2.destroyAllWindows()
