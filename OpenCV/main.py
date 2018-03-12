#!/usr/bin/python
# -*- coding: UTF-8 -*-

import cv2
import numpy

import fenci

def getImage():
    img = cv2.imread("test.bmp")
    img_shape=img.shape
    img=cv2.resize(img,(img_shape[1]/2,img_shape[0]/2),interpolation=cv2.INTER_CUBIC)
    return img

def fenci0(img):
    hsvimg=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hsv=cv2.split(hsvimg)


    th3 = cv2.adaptiveThreshold(hsv[2],255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,21,-2)

    (T, t_v) = cv2.threshold(hsv[2], 200, 255, cv2.THRESH_TOZERO_INV)#阈值化处理，阈值为：155
    (T, t_v) = cv2.threshold(t_v, 110, 255, cv2.THRESH_BINARY)#阈值化处理，阈值为：155
    #(T, t_s) = cv2.threshold(hsv[1], 150, 255, cv2.THRESH_BINARY_INV)#阈值化处理，阈值为：155
    (T, t_h) = cv2.threshold(hsv[0], 35, 255, cv2.THRESH_TOZERO_INV)#阈值化处理，阈值为：155
    (T, t_h) = cv2.threshold(t_h, 20, 255, cv2.THRESH_BINARY)#阈值化处理，阈值为：155

    (T, t_s) = cv2.threshold(hsv[1], 90, 255, cv2.THRESH_TOZERO_INV)#阈值化处理，阈值为：155
    (T, t_s) = cv2.threshold(t_s, 40, 255, cv2.THRESH_BINARY)#阈值化处理，阈值为：155

    t_hsv=cv2.bitwise_and(t_h,t_s)
    t_hsv=cv2.bitwise_and(t_hsv,t_v)


    lap_v=cv2.Canny(hsv[2],1,255)
 

    bgr=cv2.split(img)
    for i in range(3):
    	cv2.imshow(str(i),bgr[i])

    (T,t_g)=cv2.threshold(bgr[1],230,255,cv2.THRESH_TOZERO_INV)
    (T,t_g)=cv2.threshold(t_g,110,255,cv2.THRESH_BINARY)
    (T,t_r)=cv2.threshold(bgr[2],210,255,cv2.THRESH_TOZERO_INV)
    (T,t_r)=cv2.threshold(t_r,110,255,cv2.THRESH_BINARY)
    (T,t_b)=cv2.threshold(bgr[0],220,255,cv2.THRESH_TOZERO_INV)
    (T,t_b)=cv2.threshold(t_b,50,255,cv2.THRESH_BINARY)
    
    t_bgr=cv2.bitwise_and(t_b,t_g)
    t_bgr=cv2.bitwise_and(t_bgr,t_r)
    cv2.imshow('t',t_bgr)
    cv2.waitKey(0)


    diff=-cv2.absdiff(bgr[2],bgr[1])
    return t_g,0

    blurred = cv2.GaussianBlur(bgr[2], (5, 5), 0)#高斯滤波

    (T, thresh) = cv2.threshold(blurred, 205, 255, cv2.THRESH_BINARY)#阈值化处理，阈值为：155

    _1, contours, _2 = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # 根据轮廓列表，循环在原始图像上绘制矩形边界

    count_fenci=0
    for i in range(len(contours)):
        cnt = contours[i]
        x, y, w, h = cv2.boundingRect(cnt)
        if w*h>150:
            count_fenci+=1
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
    print u"粉刺：",count_fenci
    return img,count_fenci

def imgShowSave(img,savePath):
    cv2.namedWindow("Image")
    cv2.imshow("Image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #cv2.imwrite(savePath,img)
    
if __name__=='__main__':
    #cv2.cvCreateGLCM()
    img=getImage()
    cv2.imshow('src',img)
    #img,count_fenci=fenci.yanzheng(img)
    img,count_fenci=fenci0(img)
   # img=cv2.bitwise_and(img,cut)
    #imgShowSave(img,'out.bmp')
    #cv2.imshow('diff',img)
    #cv2.waitKey(0)