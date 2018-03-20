#!/usr/bin/python
# -*- coding: UTF-8 -*-

import cv2
import numpy

import pianse

def yanzheng(img):

    bgr=cv2.split(img)

    blurred = cv2.GaussianBlur(bgr[2], (5, 5), 0)#高斯滤波

    (T, thresh_r) = cv2.threshold(blurred, 205, 255, cv2.THRESH_BINARY)#阈值化处理，阈值为：205
    (T, thresh_b) = cv2.threshold(bgr[0], 205, 255, cv2.THRESH_BINARY_INV)#阈值化处理，阈值为：205
    thresh=cv2.bitwise_and(thresh_b,thresh_r)
    for i in range(thresh.shape[0]):
    	for j in range(thresh.shape[1]):
    		if bgr[2][i][j]<bgr[0][i][j] or bgr[2][i][j]<bgr[1][i][j]:
    			thresh[i][j]=0

    _1, contours, _2 = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # 根据轮廓列表，循环在原始图像上绘制矩形边界

    count_fenci=0
    mianji=0
    for i in range(len(contours)):
        cnt = contours[i]
        x, y, w, h = cv2.boundingRect(cnt)
        if w*h>150:
            mianji+=w*h
            count_fenci+=1
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
    print u"炎症: ",count_fenci,mianji
    #return img,count_fenci
    return img,mianji,count_fenci

def test():
    import pianse
    img=cv2.imread('09-44-04.bmp')
    img_shape=img.shape
    img=cv2.resize(img,(img_shape[1]/2,img_shape[0]/2),interpolation=cv2.INTER_CUBIC)
    img=pianse.pianse(img)
    ret,mianji,count_fenci=yanzheng(img)
    cv2.imshow('src',img)
    cv2.imshow('ret',ret)
    cv2.waitKey(0)

if __name__=='__main__':
	test()