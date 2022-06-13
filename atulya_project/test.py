import cv2
from cv2 import BORDER_WRAP
from cv2 import BORDER_CONSTANT
import cv2.aruco as aruco
import numpy as np
import math

def arucoid(img):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    key = getattr(aruco,f"DICT_5X5_250")
    arucodict = aruco.Dictionary_get(key)
    p = aruco.DetectorParameters_create()
    (c,i,r)= cv2.aruco.detectMarkers(img,arucodict,parameters=p)
    return (c,i,r)

y = cv2.imread('new.jpg') 
c,i,r = arucoid(y)
print('Ids of arucomarker present in image are')
for j in i:
    print(j)