#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

def getFileList(light,obj):
	ret=[]
	root='/'.join(['/home/xhq/data',light,obj])#'/home/xhq/data/.UV/fenci'
	for l in range(1,11):
		imgs=os.listdir('/'.join([root,str(l)]))
		if '.DS_Store' in imgs:
			imgs.remove('.DS_Store')
		for i in range(len(imgs)):
			imgs[i]='/'.join([str(l),imgs[i]])
		ret+=imgs
	return ret