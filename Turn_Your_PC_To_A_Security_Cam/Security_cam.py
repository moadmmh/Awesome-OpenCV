import cv2
 
cam = cv2.VideoCapture(0)
detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

Id="pic"
sampleNum=0
while(True):
    ret, img = cam.read() 
    faces = detector.detectMultiScale(img, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        
        #incrementing sample number 
        sampleNum=sampleNum+1
        #saving the captured face in the specifide directory
        cv2.imwrite(r"C:\Your directory\ "+Id +'.'+ str(sampleNum) + ".jpg", img[:])
        
        
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # break if the sample number is more than 1 picture taken
    elif sampleNum>1:
        break
cam.release()
cv2.destroyAllWindows()
