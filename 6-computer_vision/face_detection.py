import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img=cv2.imread("tefy.jpg")

resized=cv2.resize(img,(int(img.shape[1]/4),int(img.shape[0]/4)))

grey_img=cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(grey_img,
scaleFactor=1.5,
minNeighbors=5)

for x,y,w,h in faces:
    resized=cv2.rectangle(resized,(x,y),(x+w,y+h),(0,255,0))
cv2.imshow("Face Detected Image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()


