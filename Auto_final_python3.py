import numpy as np
import cv2
import math
import struct
import time
import serial
ser1=serial.Serial('com7',9600)
time.sleep(2)
detect_cascade=cv2.CascadeClassifier('haarcascade_a.xml')
detectc_cascade=cv2.CascadeClassifier('haarcascade_star.xml')
camR=cv2.VideoCapture(0)
camR.set(cv2.CAP_PROP_FRAME_WIDTH,720)
camR.set(cv2.CAP_PROP_FRAME_HEIGHT,405)
camL=cv2.VideoCapture(1)
camL.set(cv2.CAP_PROP_FRAME_WIDTH,720)
camL.set(cv2.CAP_PROP_FRAME_HEIGHT,405)
X=0
Y=0
Z=0
Xc=0
Yc=0
Zc=0
XX=0
YY=0
ZZ=0
XXc=0
YYc=0
ZZc=0
TT=0
c=0
c1=0
c2=0
c3=0
c4=0
c5=0
c6=0
c7=0
c8=0
c9=0
c10=0
c11=0
cc=0
cc1=0
cc2=0
cc3=0
cc4=0
cc5=0
cc6=0
cc7=0
cc8=0
cc9=0
cc10=0
while(True):
    a1=2000 #right
    a2=2000 #left
    tfR,frameR=camR.read()
    gray = cv2.cvtColor(frameR, cv2.COLOR_BGR2GRAY)
    detect = detect_cascade.detectMultiScale(gray, 1.3, 5)
    for (xrr,yrr,wr,hr) in detect:
        cv2.rectangle(frameR,(xrr,yrr),(xrr+wr,yrr+hr),(255,0,0),2)
        cv2.putText(frameR, "A",(xrr,yrr-50), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(255,0,0),2);
        cv2.putText(frameR, "X=" + str(X),(xrr,yrr-30), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,0,0),2);
        cv2.putText(frameR, "Y=" + str(Y),(xrr,yrr-15), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,0,0),2);
        cv2.putText(frameR, "Z=" + str(Z),(xrr,yrr), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,0,0),2);
        cv2.putText(frameR, "XX=" + str(XX),(xrr,(yrr+hr)+15), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,0,0),2);
        cv2.putText(frameR, "YY=" + str(YY),(xrr,(yrr+hr)+30), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,0,0),2);
        cv2.putText(frameR, "ZZ=" + str(ZZ),(xrr,(yrr+hr)+45), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,0,0),2);
        xr=xrr+(wr/2)
        yr=yrr+(hr/2)
        a1=(50*math.tan(32.5*3.14/180)*(xr-360)/360)-3.4
        hr=(50*math.tan(17*3.14/180)*(yr-202.5)/202.5)  
    cv2.imshow('frame_Right',frameR)
    tfL,frameL=camL.read()
    gray = cv2.cvtColor(frameL, cv2.COLOR_BGR2GRAY)
    detect = detect_cascade.detectMultiScale(gray, 1.3, 5)
    for (xll,yll,wl,hl) in detect:
        cv2.rectangle(frameL,(xll,yll),(xll+wl,yll+hl),(255,0,0),2)
        cv2.putText(frameL, "A",(xll,yll-50), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(255,0,0),2);
        cv2.putText(frameL, "X=" + str(X),(xll,yll-30), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,0,0),2);
        cv2.putText(frameL, "Y=" + str(Y),(xll,yll-15), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,0,0),2);
        cv2.putText(frameL, "Z=" + str(Z),(xll,yll), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,0,0),2);
        cv2.putText(frameL, "XX=" + str(XX),(xll,(yll+hl)+15), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,0,0),2);
        cv2.putText(frameL, "YY=" + str(YY),(xll,(yll+hl)+30), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,0,0),2);
        cv2.putText(frameL, "ZZ=" + str(ZZ),(xll,(yll+hl)+45), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,0,0),2);
        xl=xll+(wl/2)
        yl=yll+(hl/2)
        a2=(50*math.tan(32.5*3.14/180)*(xl-360)/360)+3.4
        hl=(50*math.tan(17*3.14/180)*(yl-202.5)/202.5)     
    cv2.imshow('frame_Left',frameL)
    if (a1<1000):
        if (a2<1000):
            x=((3.4*((-a2)-a1))/((-6.8)+a2-a1))
            y=(50-(340/(6.8-a2+a1)))
            X=-x
            Y=-(50-y)
            z=-(Y*hr)/50
            Z=z
            ZZ=Z+13.5
            XX=38-(Y+1)
            YY=X+27.5
            Xm=0
            Ym=0
            Zm=0
            if XX<0:
                XX=-XX
                Xm=1
            if YY<0:
                YY=-YY
                Ym=1
            if ZZ<0:
                ZZ=-ZZ
                Zm=1
            if (c11>100):
                c10=c9
                c9=c8
                c8=c7
                c7=c6
                c6=c5
                c5=c4
                c4=c3
                c3=c2
                c2=c1
                c1=c
                c=XX+YY+ZZ
                if c10>0:
                    if ((c10-c9)*(c10-c9))<=4:
                        if ((c10-c8)*(c10-c8))<=4:
                            if ((c10-c7)*(c10-c7))<=4:
                                if ((c10-c6)*(c10-c6))<=4:
                                    if ((c10-c5)*(c10-c5))<=4:
                                        if ((c10-c4)*(c10-c4))<=4:
                                            if ((c10-c3)*(c10-c3))<=4:
                                                if ((c10-c2)*(c10-c2))<=4:
                                                    if ((c10-c1)*(c10-c1))<=4:
                                                        if ((c10-c)*(c10-c))<=4:
                                                            TT=1
                                                            ser1.write(struct.pack('>BBBBBBB',XX,YY,ZZ,TT,Xm,Ym,Zm))
                                                            c11=0
                                                            print ('X=')
                                                            print (X)
                                                            print ('Y=')
                                                            print (Y)
                                                            print ('Z=')
                                                            print (Z)
    ac1=2000 #right
    ac2=2000 #left
    gray = cv2.cvtColor(frameR, cv2.COLOR_BGR2GRAY)
    detectc = detectc_cascade.detectMultiScale(gray, 1.3, 5)
    for (xrrc,yrrc,wrc,hrc) in detectc:
        cv2.rectangle(frameR,(xrrc,yrrc),(xrrc+wrc,yrrc+hrc),(0,0,255),2)
        cv2.putText(frameR, "Star",(xrrc,yrrc-50), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2);
        cv2.putText(frameR, "X=" + str(Xc),(xrrc,yrrc-30), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,255),2);
        cv2.putText(frameR, "Y=" + str(Yc),(xrrc,yrrc-15), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,255),2);
        cv2.putText(frameR, "Z=" + str(Zc),(xrrc,yrrc), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,255),2);
        cv2.putText(frameR, "XX=" + str(XXc),(xrrc,(yrrc+hrc)+15), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,255),2);
        cv2.putText(frameR, "YY=" + str(YYc),(xrrc,(yrrc+hrc)+30), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,255),2);
        cv2.putText(frameR, "ZZ=" + str(ZZc),(xrrc,(yrrc+hrc)+45), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,255),2);
        xrc=xrrc+(wrc/2)
        yrc=yrrc+(hrc/2)
        ac1=(50*math.tan(32.5*3.14/180)*(xrc-360)/360)-3.4
        hrc=(50*math.tan(17*3.14/180)*(yrc-202.5)/202.5)  
    cv2.imshow('frame_Right',frameR)
    gray = cv2.cvtColor(frameL, cv2.COLOR_BGR2GRAY)
    detectc = detectc_cascade.detectMultiScale(gray, 1.3, 5)
    for (xllc,yllc,wlc,hlc) in detectc:
        cv2.rectangle(frameL,(xllc,yllc),(xllc+wlc,yllc+hlc),(0,0,255),2)
        cv2.putText(frameL, "Star",(xllc,yllc-50), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2);
        cv2.putText(frameL, "X=" + str(Xc),(xllc,yllc-30), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,255),2);
        cv2.putText(frameL, "Y=" + str(Yc),(xllc,yllc-15), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,255),2);
        cv2.putText(frameL, "Z=" + str(Zc),(xllc,yllc), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,255),2);
        cv2.putText(frameL, "XX=" + str(XXc),(xllc,(yllc+hlc)+15), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,255),2);
        cv2.putText(frameL, "YY=" + str(YYc),(xllc,(yllc+hlc)+30), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,255),2);
        cv2.putText(frameL, "ZZ=" + str(ZZc),(xllc,(yllc+hlc)+45), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,255),2); 
        xlc=xllc+(wlc/2)
        ylc=yllc+(hlc/2)
        ac2=(50*math.tan(32.5*3.14/180)*(xlc-360)/360)+3.4
        hlc=(50*math.tan(17*3.14/180)*(ylc-202.5)/202.5)
    cv2.imshow('frame_Left',frameL)
    if (ac1<1000):
        if (ac2<1000):
            xc=((3.4*((-ac2)-ac1))/((-6.8)+ac2-ac1))
            yc=(50-(340/(6.8-ac2+ac1)))
            Xc=-xc
            Yc=-(50-yc)
            zc=-(Yc*hrc)/50
            Zc=zc
            TTc=2
            ZZc=Zc+13.5
            XXc=38-(Yc+1)
            YYc=Xc+27.5
            Xmc=0
            Ymc=0
            Zmc=0
            if XXc<0:
                XXc=-XXc
                Xmc=1
            if YYc<0:
                YYc=-YYc
                Ymc=1
            if ZZc<0:
                ZZc=-ZZc
                Zmc=1    
            if (c11>100):

                cc10=cc9

                cc9=cc8

                cc8=cc7

                cc7=cc6

                cc6=cc5

                cc5=cc4

                cc4=cc3

                cc3=cc2

                cc2=cc1

                cc1=cc








                cc=XXc+YYc+ZZc
                if cc10>0:
                    if ((cc10-cc9)*(cc10-cc9))<=4:
                        if ((cc10-cc8)*(cc10-cc8))<=4:
                            if ((cc10-cc7)*(cc10-cc7))<=4:
                                if ((cc10-cc6)*(cc10-cc6))<=4:
                                    if ((cc10-cc5)*(cc10-cc5))<=4:
                                        if ((cc10-cc4)*(cc10-cc4))<=4:
                                            if ((cc10-cc3)*(cc10-cc3))<=4:
                                                if ((cc10-cc2)*(cc10-cc2))<=4:
                                                    if ((cc10-cc1)*(cc10-cc1))<=4:
                                                        if ((cc10-cc)*(cc10-cc))<=4:
                                                            TT=2
                                                            ser1.write(struct.pack('>BBBBBBB',XXc,YYc,ZZc,TT,Xmc,Ymc,Zmc))
                                                            c11=0
                                                            print ('Xc=')
                                                            print (Xc)
                                                            print ('Yc=')
                                                            print (Yc)
                                                            print ('Zc=')
                                                            print (Zc)
    c11=c11+1
    key=cv2.waitKey(1)
    if key==ord('k'):
            break
camR.release()
camL.release()
cv2.destroyAllWindows()
