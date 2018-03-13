#!/usr/bin/python
# -*- coding: UTF-8 -*-

import cv2
import numpy

import fenci
import filelist
import pianse

def getImage(impath):
    img = cv2.imread(impath)
    img_shape=img.shape
    img=cv2.resize(img,(img_shape[1]/2,img_shape[0]/2),interpolation=cv2.INTER_CUBIC)
    return img



def imgShowSave(img,savePath):
    cv2.namedWindow("Image")
    cv2.imshow("Image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #cv2.imwrite(savePath,img)
    
if __name__=='__main__':
	f=open('out.txt','w')
	fenciList=filelist.getFileList('.UV','fenci')
	for i in fenciList:
		path='/'.join(['/home/xhq/data','.UV','fenci',i])
		print path
		level=i.split('/')[0]
		img=getImage(path)
		img=pianse.pianse(img)
		_T,count_fenci,fc=fenci.yanzheng(img)

		f.write(','.join([level,str(count_fenci),str(fc)])+'\n')
		if i=='1/Fri Sep 01 07-13-44.bmp':
			cv2.imshow('t',_T)
			cv2.waitKey(0)
	f.close()