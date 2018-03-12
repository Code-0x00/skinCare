#!/usr/bin/python
# -*- coding: UTF-8 -*-

import cv2
import numpy

def yanzheng(img):

    bgr=cv2.split(img)

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
    print u"炎症: ",count_fenci
    return img,count_fenci