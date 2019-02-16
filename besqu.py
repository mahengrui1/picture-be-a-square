#To make a jpg named 'a.jpg' be a square one 'a2.jpg' by adding 2 black slides.
#I see this code in Chinese Software Developer Network (CSDN) but it doesnt work in my python3
#so I fixed some codes grammar. The following are CSDN saying:
#-----
#作者：sh15285118586 
#来源：CSDN 
#原文：https://blog.csdn.net/sh15285118586/article/details/84033214 
#版权声明：本文为博主原创文章，转载请附上博文链接！
#-----
#Anyway the url is important.
#If u havent cv2, and have conda. just try 'pip install opencv-python'
#(For Kṣitigarbha Bodhisattva, http://tinypic.com/r/2lniu85/2)
#HENGRUI MA, 190215

from PIL import Image
from os import listdir
import math
import numpy as np
import cv2
 
def textureSquare( imgPath):
    img = Image.open(imgPath)
    width, height = img.size
    delta = width - height
    if(delta > 0):
        repeat = delta / height
        result = Image.new(img.mode, (width, height + delta))
        region1 = img.crop((0, height - (delta - repeat * height), width, height))
        result.paste(region1, box = (0, 0))
        result.paste(img, box = (0, int(delta - repeat * height/2)))
        return result
    elif(delta < 0):
        delta = abs(delta)
        repeat = delta / width
        result = Image.new(img.mode, (width + delta, height))
        region1 = img.crop((0, 0, delta - repeat * width, height))
        result.paste(region1, box = (0, 0))
        result.paste(img, box = (int(delta - repeat * width/2), 0))
        return result
    else:
        return img
 
 
def textureTransform( imgPath, offsetX, offsetY, uvScale):
    imgOriginal = Image.open(imgPath)
 
 
img = textureSquare("a.jpg")
# print img.size
img.save("a2.jpg")
