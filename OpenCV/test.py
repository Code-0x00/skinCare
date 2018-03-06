#!/usr/bin/python
# -*- coding: UTF-8 -*-
import cv2

def main():
    img = cv2.imread("test.1.bmp")
    imgGray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    (b,c)=imgGray.shape
    print imgGray.shape,b,c
    cutt=imgGray[0]
    print imgGray[0][0]
    #cv2.imshow('ii',imgGray)
    #cv2.waitKey(0)
    return 0
    
main()