import os
import crop

def sysShell():
	makeUpList=os.listdir('makeUp')
	notMakeUpList=os.listdir('notMakeUp')
	if not os.path.exists("./xData"):
		os.system("mkdir xData")
	headName='xData/I5C0U0N'
	for i in range(64):
		print 'C0U0',i
		crop.crop('/'.join(['makeUp',makeUpList[i]]),headName+"%02d"%(i))
	headName='xData/I5C1U0N'
	for i in range(64):
		print 'C1U0',i
		crop.crop('/'.join(['notMakeUp',notMakeUpList[i]]),headName+"%02d"%(i))
	headName='xData/I5C0U2N'
	for i in range(64,85):
		print 'C0U2',i
		crop.crop('/'.join(['makeUp',makeUpList[i]]),headName+"%02d"%(i))
	headName='xData/I5C1U2N'
	for i in range(64,85):
		print 'C1U2',i
		crop.crop('/'.join(['notMakeUp',notMakeUpList[i]]),headName+"%02d"%(i))
sysShell()
	