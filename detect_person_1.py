import cv2
import numpy as np 
import imutils

protopath = "MobileNetSSD_deploy.prototxt"
modelpath = "MobileNetSSD_deploy.caffemodel"

detector = cv2.dnn.readNetFromCaffe(prototxt=protopath, caffeModel=modelpath)

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat", 
"bottle", "bus", "car", "cat", "chair", "cow", "diningtable", 
"dog", "horse", "motorbike", "person", "pottedplant", "sheep", 
"sofa", "train", "tvmonitor"]

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,1000)


def countPeople():
    #image = cv2.imread('image/4.png') #hình
    #image = imutils.resize(image, width=600)#hình
    #cap = cv2.VideoCapture("video/1.mp4") #video
    #success, image = cap.read() #video
    success, img = cap.read() #cam
    image = cv2.flip(img,1) #cam
    (H, W) = image.shape[:2]
    count = 0
    blob = cv2.dnn.blobFromImage(image, 0.007843, (W, H), 127.5)
    detector.setInput(blob)
    person_detections = detector.forward()

    for i in np.arange(0, person_detections.shape[2]):
        confidence = person_detections[0, 0, i, 2]
        if confidence > 0.5:
            idx = int(person_detections[0, 0, i, 1])
            if CLASSES[idx] != "person":
                continue
            else:
                count = count + 1

            person_box = person_detections[0, 0, i, 3:7] * np.array([W, H, W, H])
            (starX, StarY, endX, endY) = person_box.astype("int")
            cv2.rectangle(image, (starX, StarY), (endX, endY), (0, 0, 255), 2)
   
    
    cv2.imshow("abc",image)
    cv2.waitKey(1)
    #cv2. destroyAllWindows()
    return count


while True:
    a = countPeople()
    print("số người là: " + str(a))
