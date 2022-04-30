import cv2
cam=cv2.VideoCapture(2)

while True:
    tf,frame=cam.read()
    cv2.imshow('frame',frame)
    key=cv2.waitKey(1)
    if key==ord('k'):
            break
cam.release()
cv2.destroyAllWindows()