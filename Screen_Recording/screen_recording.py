import numpy as np 
import cv2 

# for windows, mac users
from PIL import ImageGrab
# for linux users
#import pyscreenshot as ImageGrab

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("output.avi", fourcc, 5.0, (1366, 768))

while True:
	img = ImageGrab.grab()
	img_np = np.array(img)

	frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

        #if you want to see the creen tho there'll be a lot of them opened  
        #so whenever there  it goes inside the loop it shows a new one
	#it'3 better to avoid it 
        #cv2.imshow('screen',frame)

	out.write(frame)
        #if u show thw screen to quit pres 'Esc'  
	if cv2.waitKey(1) == 27:
		break

out.release()
cv2.destroyAllWindows()
