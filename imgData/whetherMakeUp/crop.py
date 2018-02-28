import cv2
import numpy as np
def crop(imgName,saveNameHead):
	img=cv2.imread(imgName)

	for i in range(4):
		img256x1280=img[i*256:i*256+256]
		img1280x256=np.transpose(img256x1280,(1,0,2))

		for j in range(5):
			savename='.'.join([saveNameHead,str(i),str(j),'bmp'])
			tmp=img1280x256[j*256:j*256+256]
			img256x256=np.transpose(tmp,(1,0,2))
			cv2.imwrite(savename,img256x256)