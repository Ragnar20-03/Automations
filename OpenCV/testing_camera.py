import cv2 
 
camera = cv2.VideoCapture(0)
camera.set(3,640) # set Width
camera.set(4,480) # set Height
while (1): 
    ret ,frame = camera.read()
    cv2.imshow("Frame" , frame)
    
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break
camera.release()
cv2.destroyAllWindows()