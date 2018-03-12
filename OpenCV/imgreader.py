#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
rootPath='/home/xhq/data/'
l=os.listdir('/home/xhq/data/')
print l

l2=os.listdir(rootPath+l[1])
print l2
l3=os.listdir(rootPath+l[1]+'/'+l2[0])
print l3