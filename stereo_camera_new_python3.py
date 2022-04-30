import cv2
import numpy as np
import math
import struct
import time
import serial

time.sleep(2)


cam_wid = 720   # set width and height of camera output image
cam_ht = 405

camR=cv2.VideoCapture(2)  #assign wecams
camR.set(cv2.CAP_PROP_FRAME_WIDTH,cam_wid)   #set height and width of camera image
camR.set(cv2.CAP_PROP_FRAME_HEIGHT,cam_ht)
camL=cv2.VideoCapture(4)
camL.set(cv2.CAP_PROP_FRAME_WIDTH,cam_wid)
camL.set(cv2.CAP_PROP_FRAME_HEIGHT,cam_ht)

detect_cascade=cv2.CascadeClassifier('/home/jayesh/Desktop/cv2_test/haarcascade_a.xml')   #load image classifiers


X=0   #initial value of detected coordinates
Y=0    # taking Y as height
Z=0    # taking Z as depth from camera as origin

dist = 40  #discance between 2 cameras in mm

h_ang = math.radians(25)   #horizontal angle range of camera
v_ang = math.radians(20)   #vertical angle range of camera

f = 10  # in mm    #assume focal distance for camera ie discance between frame projection and camera origin




while True:
    
    x_r = 10000 #right  # just to make sure tha both camera are detecting the image before procedding further calculations to avoid errors
    x_l =10000 #left
    
    
    # first read image
    # detect objects
    # display bounding box and texts
    # identify the position in frame
    
    
    tfR,frameR=camR.read()   #read te camera frame from right camera
    grayR = cv2.cvtColor(frameR, cv2.COLOR_BGR2GRAY)  #convert the image to grayscale
    detectR = detect_cascade.detectMultiScale(grayR, 1.3, 5)  # detect object in image
    for (org_x_r,org_y_r,w_r,h_r) in detectR:   #origin, wifth and height of detected image  # origin starts from top left and goes positive in downward and rightward direction
        cv2.rectangle(frameR,(org_x_r,org_y_r),( org_x_r + w_r , org_y_r + h_r ),(255,0,0),2)  # draw rectangle around detected object
        cv2.putText(frameR, "A",(org_x_r,org_y_r-50), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(255,0,0),2);  # show name of object detected 
        cv2.putText(frameR, "X = " + str(X),(org_x_r,org_y_r-30), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,0,0),2);  # show coordinated of object detected
        cv2.putText(frameR, "Y = " + str(Y),(org_x_r,org_y_r-15), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,0,0),2);
        cv2.putText(frameR, "Z (depth) = " + str(Z),(org_x_r,org_y_r), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,0,0),2);
                  
        x_r = (org_x_r + (w_r/2)) - (cam_wid/2)   # center x coordinate of object and transforming it to make origin at center of image
        y_r = -(org_y_r + (h_r/2)) + (cam_ht/2)  # center y coordinate of object and transforming it yo make origin at center of image
        
        x_r = (x_r / (cam_wid/2)) * (f * math.tan(h_ang/2))  # in mm  # converting the pixel coordinate to distance, assuming that the frame is formed at a distance f from camera
        y_r = (y_r / (cam_ht/2)) * (f * math.tan(v_ang/2))
               
    cv2.imshow('frame_Right',frameR)
    
    tfL,frameL=camL.read()   #read te camera frame from left camera
    grayL = cv2.cvtColor(frameL, cv2.COLOR_BGR2GRAY)  #convert the image to grayscale
    detectL = detect_cascade.detectMultiScale(grayL, 1.3, 5)  # detect object in image
    for (org_x_l,org_y_l,w_l,h_l) in detectL:   #origin, wifth and height of detected image  # origin starts from top left and goes positive in downward and rightward direction
        cv2.rectangle(frameL,(org_x_l,org_y_l),( org_x_l + w_l , org_y_l + h_l ),(255,0,0),2)  # draw rectangle around detected object
        cv2.putText(frameL, "A",(org_x_l,org_y_l-50), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(255,0,0),2);  # show name of object detected 
        cv2.putText(frameL, "X = " + str(X),(org_x_l,org_y_l-30), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,0,0),2);  # show coordinated of object detected
        cv2.putText(frameL, "Y = " + str(Y),(org_x_l,org_y_l-15), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,0,0),2);
        cv2.putText(frameL, "Z (depth) = " + str(Z),(org_x_l,org_y_l), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,0,0),2);
                  
        x_l = (org_x_l + (w_l/2)) - (cam_wid/2)   # center x coordinate of object and transforming it to make origin at center of image
        y_l = -(org_y_l + (h_l/2)) + (cam_ht/2)  # center y coordinate of object and transforming it yo make origin at center of image
        
        x_l = (x_l / (cam_wid/2)) * (f * math.tan(h_ang/2))  # in mm  # converting the pixel coordinate to distance, assuming that the frame is formed at a distance f from camera
        y_l = (y_l / (cam_ht/2)) * (f * math.tan(v_ang/2))
               
    cv2.imshow('frame_Left',frameL)
    
    
    ## Now start with stereo vision calculation to identify depth
    if x_r < 10000 and x_l < 10000:
        
        # Using similar triangle approach
        # Z/dist = Z-f/(dist-x_l+x_r)
        # (dist-x_l+x_r)/dist = 1 - f/Z
        # f/Z = 1 - (dist-x_l+x_r)/dist
        # f/Z = (x_l - x_r)/dist
        # Z = (f*dist) / (x_l - x_r)
        
        Z = (f*dist) / (x_l - x_r)  # in mm
        
        # X = ((Z * (x_l/f) ) - (dist/2) )   or  ( (Z * (x_r/f) ) + (dist/2) ) 
        # Y = Z * (((y_l + y_r)/2)/f)  
        
        X = ((Z * (x_l/f) ) - (dist/2) ) 
        Y = Z * (((y_l + y_r)/2)/f)     
        
        
        X = X/10   ## converting the position to centimeters
        Y = Y/10
        Z = Z/10
    
    
    print ('\n \n X = ',X)
    print ('Y = ',Y)
    print ('Z (depth) = ',Z)
            
    
    # Now approach for frame transformation
    
    
    
    
    
    
    key=cv2.waitKey(1)
    if key==ord('k'):
            break






camR.release()
camL.release()
cv2.destroyAllWindows()