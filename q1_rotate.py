
import numpy as np
import cv2
import math
angle=30
radians = float(angle*(math.pi/180))
img = cv2.imread('scale.png',0)
width,height = img.shape


maxx=int(math.sqrt(width**2+height**2))
maxy=maxx
a=int(width/2)
b=int(height/2)
rotate_img = np.zeros((maxx,maxy),dtype="uint8")
for i in range(0,maxx):
    for j in range(0,maxy):


        x=(i-a)*math.cos(radians)+(j-b)*math.sin(radians)+a
        y=-(i-a)*math.sin(radians)+(j-b)*math.cos(radians)+b

          
        if x<width and y<height and x>0 and y>0:
            rotate_img[i, j] = img[int(x),int(y)]
 



cv2.imwrite("rotated"+str(angle)+".png", rotate_img)       
