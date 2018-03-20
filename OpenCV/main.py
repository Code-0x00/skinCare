#!/usr/bin/python
# -*- coding: UTF-8 -*-

import cv2
import numpy

import fenci
import filelist
import pianse
import glcm

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
	fenciList=filelist.getFileList('.sunLight','zhouwen')
	for i in fenciList:
		path='/'.join(['/home/xhq/data','.sunLight','zhouwen',i])
		print path
		level=i.split('/')[0]
		img=getImage(path)

		img=pianse.pianse(img)
		img_lab=cv2.cvtColor(img,cv2.COLOR_BGR2Lab)
		img_gray=cv2.split(img_lab)[0]

		glcm_0=glcm.getGlcm(img_gray, 1,0)
    #glcm_1=getGlcm(src_gray, 0,1)
    #glcm_2=getGlcm(src_gray, 1,1)
    #glcm_3=getGlcm(src_gray, -1,1)

		asm,con,eng,idm=glcm.feature_computer(glcm_0)

		f.write(','.join([level,str(asm),str(con),str(eng),str(idm)])+'\n')

	f.close()