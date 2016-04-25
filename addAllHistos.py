import glob, subprocess

importDir = "HistoFiles/*"
doSubmit=True

fileList = glob.glob(importDir)

fileList = [x[:x.rfind("_")] for x in fileList]

counted = dict((x,fileList.count(x)) for x in set(fileList))

for item in counted:
	if counted[item]<2: continue
	command = " "
	for i in range(1,counted[item]+1):
		command += item+"_"+str(i)+".root " 

	haddCommand = "hadd -f "+item+".root "+command
	rmCommand = "rm "+ command
	print haddCommand

	if doSubmit:
		subprocess.call(haddCommand, shell=True)
		subprocess.call(rmCommand, shell=True)
