
import cv2 
import numpy as np
from google.colab.patches import cv2_imshow
import matplotlib.pyplot as plt


left = cv2.imread("l3.png")
right = cv2.imread('r3.png')
leftG = cv2.cvtColor(left, cv2.COLOR_BGR2GRAY)
rightG = cv2.cvtColor(right, cv2.COLOR_BGR2GRAY)

leftrsz=cv2.resize(leftG, (0,0),fx=0.5,fy=0.5)
rightrsz=cv2.resize(rightG, (0,0),fx=0.5,fy=0.5)

#for window size = 1
disparity_1 = np.zeros(leftG.shape)
#disparity_1_SSD = np.zeros(leftG.shape)
 
for i in range(leftG.shape[0]):
   for j in range(leftG.shape[1]):
     min=99999
     idx=-1
     for x in range(leftG.shape[1]):
       temp = np.sum(np.abs(leftG[i][j] - rightG[i][x]))
       if(min > temp):
        min = temp
        idx=x
          
        
  
     disparity_1[i][j]= (np.abs(idx-j))
   


     

     


#print(leftrsz.shape)

cv2_imshow(disparity_1)
# print(disparity_1.shape)
# cv2_imshow(leftG)
# cv2_imshow(rightG)
left = cv2.imread("l3.png")
right = cv2.imread('r3.png')
leftG = cv2.cvtColor(left, cv2.COLOR_BGR2GRAY)
rightG = cv2.cvtColor(right, cv2.COLOR_BGR2GRAY)

leftrsz=cv2.resize(leftG, (0,0),fx=0.5,fy=0.5)
rightrsz=cv2.resize(rightG, (0,0),fx=0.5,fy=0.5)

#for window size = 1
disparity_1 = np.zeros(leftG.shape)
#disparity_1_SSD = np.zeros(leftG.shape)
 
for i in range(leftG.shape[0]):
   for j in range(leftG.shape[1]):
     min=99999
     idx=-1
     for x in range(leftG.shape[1]):
       temp = np.sum((np.abs(leftG[i][j] - rightG[i][x]))**2)
       if(min > temp):
        min = temp
        idx=x
          
        
    #disparity_1[i][j]= (idx*255/leftrsz.shape[1]) 
     disparity_1[i][j]= (np.abs(idx-j))  

cv2_imshow(disparity_1)    
def getDisparity(SD,Window_Size):
  left = cv2.imread("l3.png")
  right = cv2.imread('r3.png')
  leftG = cv2.cvtColor(left, cv2.COLOR_BGR2GRAY)
  rightG = cv2.cvtColor(right, cv2.COLOR_BGR2GRAY)
  rows=leftG.shape[0]
  col=leftG.shape[1]

  leftrsz=cv2.resize(leftG, (0,0),fx=0.5,fy=0.5)
  rightrsz=cv2.resize(rightG, (0,0),fx=0.5,fy=0.5)
  disparity_1 = np.zeros(leftG.shape)

  for i in range (int(Window_Size/2) , rows-int(Window_Size/2)):
    for j in range(int(Window_Size/2),col-int(Window_Size/2)):
      min=99999
      idx=-1
      windowR = rightG[i-int(Window_Size/2):i+int(Window_Size/2)+1,j-int(Window_Size/2):j+int(Window_Size/2)+1]
      for x in range (int(Window_Size/2),col-int(Window_Size/2)):
        windowL=leftG[i-int(Window_Size/2):i+int(Window_Size/2)+1 , x-int(Window_Size/2) : x+int(Window_Size/2)+1]
        if (SD == 1 ):
          temp = np.sum(np.abs(windowL-windowR))
        else:
          temp= np.sum((np.abs(windowL-windowR))**2)
        if(min > temp):
         min = temp
         idx=x


      disparity_1[i][j]= np.abs(idx-j)


  return disparity_1

