import matplotlib.pyplot as plt
import cv2 

img = cv2.imread("/Users/ragnar20-03/Desktop/pythondemo.png" , cv2.IMREAD_COLOR)
print (img.shape)

gray_image = cv2.cvtColor(img  ,cv2.COLOR_BGR2GRAY)
print(gray_image)

face_Classfier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

face = face_Classfier.detectMultiScale(
    gray_image , scaleFactor = 1.1 ,  minNeighbors=5, minSize=(40, 40)
)

for (x, y, w, h) in face:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)
print (" Count of faces is : " , len(face))
    
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)




plt.figure(figsize=(20,10))
plt.imshow(img_rgb)
plt.axis('off')
cv2.imshow("Image" , img)

cv2.waitKey(10000)