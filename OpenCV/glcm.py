#!/usr/bin/python
# -*- coding: UTF-8 -*-
import cv2
gray_level = 16

def maxGrayLevel(img):
    (height,width,d)=img.shape
    for j in range(height):
        for i in range(width):
            if srcdata[i][j] > max_gray_level:
                max_gray_level = srcdata[i][j]
    return max_gray_level+1

def getGlcm(input,d_x,d_y):
    dst=[[0 for i in range(gray_level)] for j in range(gray_level)]
    (height,width) = input.shape
    
    max_gray_level=maxGrayLevel(input)

    if max_gray_level > gray_level:##//若灰度级数大于16，则将图像的灰度级缩小至16级，减小灰度共生矩阵的大小。
        for i in range(height):
            for j in range(width):#j in range(width):#
                srcdata[j][i] = srcdata[j][i]*gray_level / max_gray_level

    for i in range(height-d_y):
        for j in range(width-d_x):#j in range(width-1):#
             rows = srcdata[j][i]
             cols = srcdata[j + d_x][i+d_y]
             dst[rows][cols]+=1
    return dst

def feature_computer(src, Asm, Eng, Con, Idm):#(Mat&src, double& Asm, double& Eng, double& Con, double& Idm)#//计算特征值

    height = src.rows
    width = src.cols
    total = 0
    for i in range(height):#
        int*srcdata = src.ptr<int>(i)
        for j in range(width):#
            total += srcdata[j]##//求图像所有像素的灰度值的和
    #Mat copy
    copy.create(height, width, CV_64FC1)
    for i in range(height):#
        int*srcdata = src.ptr<int>(i)
        double*copydata = copy.ptr<double>(i)
        for j in range(width):#
            copydata[j]=float(srcdata[j]/float(total))#//图像每一个像素的的值除以像素总和
    for i in range(height):#
        double*srcdata = copy.ptr<double>(i)
        for j in range(width):#
            Asm += srcdata[j] * srcdata[j]#//能量
            if srcdata[j]>0:
                Eng -= srcdata[j] * log(srcdata[j])#//熵
            Con += (double)(i - j)*(double)(i - j)*srcdata[j]#//对比度
            Idm += srcdata[j] / (1 + (double)(i - j)*(double)(i - j))#//逆差矩

def main():
    img = cv2.imread("test.0.bmp")
    imgGray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('ii',imgGray)
    return 0

    #Mat dst_horison, dst_vertical, dst_45, dst_135
    src = imread("C:\\Users\\aoe\\Desktop\\Visual C+\\Visual C+\\chapter08\\pic\\healthy\\201.bmp")
    if src.empty():
        return -1
    #Mat src_gray
    ##//src.create(src.size(), CV_8UC1)
    ##//src_gray = Scalar::all(0)
    cvtColor(src, src_gray, COLOR_BGR2GRAY)
    ##//src =( Mat_<int>(6, 6) << 0, 1, 2, 3, 0, 1, 1, 2, 3, 0, 1, 2, 2, 3, 0, 1, 2, 3, 3, 0, 1, 2, 3, 0, 0, 1, 2, 3, 0, 1, 1, 2, 3, 0, 1, 2 )
    ##//src = (Mat_<int>(4, 4) << 1, 17, 0, 3,3,2,20,5,26,50,1,2,81,9,25,1)
    getglcm_horison(src_gray, dst_horison)
    getglcm_vertical(src_gray, dst_vertical)
    getglcm_45(src_gray, dst_45)
    getglcm_135(src_gray, dst_135)
    eng_horison=0, con_horison=0, idm_horison=0, asm_horison=0
    feature_computer(dst_horison, asm_horison, eng_horison, con_horison, idm_horison)
    cout << "asm_horison:" << asm_horison << endl
    cout << "eng_horison:" << eng_horison << endl
    cout << "con_horison:" << con_horison << endl
    cout << "idm_horison:" << idm_horison << endl
    system("pause")
    return 0
