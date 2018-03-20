#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import matplotlib.pyplot as plt

def fenci():
	f=open('out.txt','r')
	lines=f.readlines()
	datax=[i for i in range(len(lines))]

	datay=[]
	numcut=0
	for l in range(1,11):
		count=0
		y=[]
		for line in lines:
			t=line.split(',')
			if l==int(t[0]):
				y.append(float(t[3]))
				numcut+=1
		y.sort()
		datay=datay+y
		ty=[1.5,3.0000]
		tx=[numcut-0.5,numcut-0.5]
		plt.plot(tx,ty,'r')


	plt.plot(datax,datay,'*')
	plt.show()


if __name__=='__main__':
	fenci()