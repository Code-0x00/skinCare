#!/usr/bin/python
# -*- coding: UTF-8 -*-
import cv2
import math
gray_level = 16

def maxGrayLevel(img):
    max_gray_level=0
    (height,width)=img.shape
    print height,width
    for y in range(height):
        for x in range(width):
            if img[y][x] > max_gray_level:
                max_gray_level = img[y][x]
    return max_gray_level+1

def getGlcm(input,d_x,d_y):
    srcdata=input.copy()
    ret=[[0.0 for i in range(gray_level)] for j in range(gray_level)]
    (height,width) = input.shape
    
    max_gray_level=maxGrayLevel(input)

    if max_gray_level > gray_level:##//若灰度级数大于16，则将图像的灰度级缩小至16级，减小灰度共生矩阵的大小。
        for j in range(height):
            for i in range(width):#j in range(width):#
                srcdata[j][i] = srcdata[j][i]*gray_level / max_gray_level

    for j in range(height-d_y):
        for i in range(width-d_x):#j in range(width-1):#
             rows = srcdata[j][i]
             cols = srcdata[j + d_y][i+d_x]
             ret[rows][cols]+=1.0

    for i in range(gray_level):
    	for j in range(gray_level):
    		ret[i][j]/=float(height*width)

    return ret

def feature_computer(p):
	Con=0
	Eng=0
	Asm=0
	Idm=0
	for i in range(gray_level):
		for j in range(gray_level):
			Con+=(i-j)*(i-j)*p[i][j]
			Asm+=p[i][j]*p[i][j]
			Idm+=p[i][j]/(1+(i-j)*(i-j))

			if p[i][j]>0.0:
				Eng+=p[i][j]*math.log(p[i][j])
	return Asm,Con,-Eng,Idm

def main():

    src = cv2.imread("zw.1.1.bmp")
    img_shape=src.shape
    src=cv2.resize(src,(img_shape[1]/2,img_shape[0]/2),interpolation=cv2.INTER_CUBIC)
    #if src==None:
    #    return -1
    
    src_gray=cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    glcm_0=getGlcm(src_gray, 1,0)
    #glcm_1=getGlcm(src_gray, 0,1)
    #glcm_2=getGlcm(src_gray, 1,1)
    #glcm_3=getGlcm(src_gray, 1,1)

    asm,con,eng,idm=feature_computer(glcm_0)
    

    print asm,con,eng,idm
main()