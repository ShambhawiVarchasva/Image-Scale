import numpy as np
import cv2
import math



def GetBilinearPixel(imArr, posX, posY):
        out = []
 
      
        modXi = int(posX)
        modYi = int(posY)
        modXf = posX - modXi
        modYf = posY - modYi
        modXiPlusOneLim = min(modXi+1,imArr.shape[1]-1)
        modYiPlusOneLim = min(modYi+1,imArr.shape[0]-1)
 
      

        bl = imArr[modYi, modXi]
        br = imArr[modYi, modXiPlusOneLim]
        tl = imArr[modYiPlusOneLim, modXi]
        tr = imArr[modYiPlusOneLim, modXiPlusOneLim]
 
               
        b = modXf * br + (1. - modXf) * bl
        t = modXf * tr + (1. - modXf) * tl
        pxf = modYf * t + (1. - modYf) * b
        out=(int(pxf+0.5))
       
        return out

img= np. array([[0,2,4],[2,4,6],[4,6,8]])
w1,h1 = img.shape


#scale_x=2
#scale_y=2
print("Original Image")
print(img)
w2= 5
h2=5

img_nn = np.empty((w2,h2), dtype=np.uint8)
x_ratio=float(w1/float(w2))
y_ratio=float(h1/float(h2))


for i in range(0,w2):
    for j in range(0,h2):
        p_x=math.floor(j*x_ratio)
        p_y=math.floor(i*y_ratio)
      
        img_nn[j,i]=img[int(p_x),int(p_y)]
cv2.imwrite("nn_2d.png", img_nn) 

print("nearest neighbor")
print(img_nn)
img_bl = np.empty((w2,h2), dtype=np.uint8)
for i in range(0,w2):
    for j in range(0,h2):
        orir = i * x_ratio #Find position in original image
        oric = j * y_ratio
        
        img_bl[i, j]= GetBilinearPixel(img, oric, orir)
cv2.imwrite("bl_2d.png", img_bl) 
print("Bilinear interpolation")
print(img_bl)


