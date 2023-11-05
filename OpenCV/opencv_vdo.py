import cv2 

vdo_capture = cv2.VideoCapture(0)

face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

def detect_bounding_box(vid):
    print("Inside Detect Boundary ....")
    gray_image  = cv2.cvtColor(vid , cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image , 1.1 , 5 , minSize=(40 , 40))
    for (x , y , w , h ) in faces : 
        cv2.rectangle(vid , (x , y ) , (x + w , y + h ) , (0 , 255 , 0) , 4)
    return faces , len(faces)

while True:

    result, video_frame = vdo_capture.read()  # read frames from the video
    if result is False:
        break  # terminate the loop if the frame is not read successfully

    faces , count = detect_bounding_box(
        video_frame
    )  # apply the function we created to the video frame

    print("iCount is : " , count)
    cv2.imshow(
        "Face Detect", video_frame
    )  # display the processed frame in a window named "Face Detect"

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

vdo_capture.release()
cv2.destroyAllWindows()