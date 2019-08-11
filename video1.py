import time
import cv2
import mss
import numpy as np
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def nothing(x):
    pass

scr_rsl = (1920,1080)
box_size = (800,800)
center = (scr_rsl[0]//2 - box_size[0]//2,
          scr_rsl[1]//2- box_size[1]//2)
cv2.namedWindow('trackbars')

## create trackbars
cv2.createTrackbar('lh', 'trackbars', 0, 179, nothing)
cv2.createTrackbar('ls', 'trackbars', 0, 255, nothing)
cv2.createTrackbar('lv', 'trackbars', 0, 255, nothing)
cv2.createTrackbar('uh', 'trackbars', 179, 179, nothing)
cv2.createTrackbar('us', 'trackbars', 255, 255, nothing)
cv2.createTrackbar('uv', 'trackbars', 255, 255, nothing)


with mss.mss() as sct:
    box = {'top': 0, 'left': 0,
           'width': box_size[0], 'height': box_size[1]}

    while 'Screen capturing':
        t = time.time()
        
        ## Get trackbars' positions
        lh = cv2.getTrackbarPos('lh','trackbars')
        ls = cv2.getTrackbarPos('ls','trackbars')
        lv = cv2.getTrackbarPos('lv','trackbars')
        uh = cv2.getTrackbarPos('uh','trackbars')
        us = cv2.getTrackbarPos('us','trackbars')
        uv = cv2.getTrackbarPos('uv','trackbars')
        
        #print('lower : {0}, {1}, {2}|| upper: {3}, {4}, {5}'
         #     .format(lh,ls,lv,uh,us,uv))
        
        img = np.array(sct.grab(box)) #take box as image source
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        #red color range
        lower_red = np.array([0,230,0],np.uint8)
        upper_red = np.array([41,255,255],np.uint8)
        #lower_red = np.array([lh,ls,lv],np.uint8)
        #upper_red = np.array([uh,us,uv],np.uint8)
        
        #red mask
        red = cv2.inRange(hsv, lower_red, upper_red)
        #result
        res = cv2.bitwise_and(img, img, mask = red)

        #Filters
        kernel = np.ones((5,5),np.uint8)
        erosion = cv2.erode(red,kernel,iterations = 1)
        dilation = cv2.dilate(red,kernel,iterations = 1)
        '''
        ## FPS counter on screen
        fps = round(1 / (time.time()-t))
        cv2.putText(res, 'FPS: {}'.format(fps),(10,20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0))
        '''
        ## Tracking the Red Color
        contours, hierarchy  = cv2.findContours(red,
                                                cv2.RETR_TREE,
                                                cv2.CHAIN_APPROX_SIMPLE)
        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if(area>200):
                x,y,w,h = cv2.boundingRect(contour)
                target_center = (x+w//2,y+h//2)
                img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                #print(x+w//2,y+h//2)
                #cv2.circle(res,(x+w//2,y+h//2), 2, (0,255,0), -1)
                cv2.putText(img,"target",(x,y),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.7,
                            (0,0,255))
                print('working')
                print('...')
                
                #click(target_center[0],target_center[1])
                #time.sleep(0.1)

        
        #points = cv2.findNonZero(erosion) #
        #avg = np.mean(points, axis=0) #
        
        
        #cv2.circle(res,(int(avg[0][0]),int(avg[0][1])), 25, (0,255,0), 2)
        #cv2.rectangle(res,(10,10),(20,20),(179, 255, 255),2)
        
        ## Display the picture
        #cv2.imshow('erosion', erosion)
                
        #cv2.imshow('dilation', dilation)
        #cv2.imshow('red', red)
        
        cv2.imshow('img', img)
        #cv2.imshow('res', res)
        

        # Display the picture in grayscale
        #cv2.imshow('gray', cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))

        #print('fps: {0}'.format(1 / (time.time()-t)))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

