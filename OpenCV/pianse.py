#!/usr/bin/python
# -*- coding: UTF-8 -*-

import cv2
import numpy

def getImage(impath):
    img = cv2.imread(impath)
    img_shape=img.shape
    img=cv2.resize(img,(img_shape[1]/2,img_shape[0]/2),interpolation=cv2.INTER_CUBIC)
    return img


def getMean(img):
	#print type(img[0][0])
	sum=0.0
	for i in range(img.shape[0]):
		for j in range(img.shape[1]):
			sum+=float(img[i][j])
	return sum/(img.shape[0]*img.shape[1])

def getMax(img):
	ret=0
	for i in range(img.shape[0]):
		for j in range(img.shape[1]):
			if img[i][j]>ret:
				ret=img[i][j]
	return ret

def pianse(img):
	img_lab=cv2.cvtColor(img, cv2.COLOR_BGR2Lab)

	lab=cv2.split(img_lab)
	aMean=getMean(lab[1])
	bMean=getMean(lab[2])

	for i in range(img.shape[0]):
		for j in range(img.shape[1]):
			lab[1][i][j]=numpy.uint8(float(lab[1][i][j])/aMean*128.0)
			lab[2][i][j]=numpy.uint8(float(lab[2][i][j])/bMean*128.0)
	ret=cv2.merge(lab)
	ret=cv2.cvtColor(ret,cv2.COLOR_Lab2BGR)
	
	return ret
    
if __name__=='__main__':
	#img=getImage('t8.bmp')
	img=getImage('09-32-18.bmp')
	cv2.imshow('src',img)
	img=pianse(img)
	cv2.imshow('i',img)

	cv2.waitKey(0)
	cv2.imwrite('x.bmp',img)
