import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    for j in range(9):
        print ( "Grid:"+str(j))
        r = cv.selectROI("select the area", frame)
        i=0
        a = r[i]+r[i+2]
        b= r[i+1]+r[i+3]
        c = (r[i]+a)/2
        d = (r[i+1]+b)/2
        print(r[i])
        print(r[i+1])
        print (r[i]+r[i+2])
        print (r[i+1]+r[i+3])
        print(c)
        print (d)




    # Display the resulting frame
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
