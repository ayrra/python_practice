import cv2
import glob

images=glob.glob('*.jpg')

for image in images:
    img=cv2.imread(image,1)
    resized_image=cv2.resize(img,(100,100))
    cv2.imwrite("resized_"+image,resized_image)