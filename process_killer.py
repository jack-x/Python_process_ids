import time
import os
import subprocess
import signal

def getProcessList():
	ret =str( os.system("ps -ef > processes.txt"))
	f = open("processes.txt",'r')
	lines = f.readlines()
	os.remove("processes.txt")
	lines.pop(0)
	lines.pop(-1)
	processList = list()
	pidlist = list()
	for x in lines:
		xx = x.split()
		processList.append([xx[0],xx[1],xx[7]])
		pidlist.append(xx[1])
	return processList

def getAllPids():
	ret =str( os.system("ps -ef > processes.txt"))
	f = open("processes.txt",'r')
	lines = f.readlines()
	os.remove("processes.txt")
	lines.pop(0)
	lines.pop(-1)
	processList = list()
	pidlist = list()
	for x in lines:
		xx = x.split()
		processList.append([xx[0],xx[1],xx[7]])
		pidlist.append(xx[1])
	return pidlist
	
	
while True:
	pidlist1 = getAllPids()
	processlist1 = getProcessList()
	p1 = subprocess.Popen(["/usr/bin/python3.6","/home/naman/Desktop/code/process1.py"],stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
	time.sleep(3)
	p2 = subprocess.Popen(["/usr/bin/python3.6","/home/naman/Desktop/code/process2.py"],stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
	time.sleep(3)
	
	pidlist2 = getAllPids()
	processlist2 = getProcessList()
	
	newProcesses = list()
	for x in pidlist2:
		if x not in pidlist1:
			newProcesses.append(x)
	print(newProcesses)
	
	p1.terminate()
	p2.terminate()
	print("##############")
	
	time.sleep(6)
	pidlist2 = getAllPids()
	processlist2 = getProcessList()
	
	newProcesses = list()
	for x in pidlist2:
		if x not in pidlist1:
			newProcesses.append(x)
	print("After Process Termination")
	print(newProcesses)
	print("############")
	
	
	for x in newProcesses:
		for y in processlist2:
			if x in y:
				print(x)
				print(y)
	pidlist2 = getAllPids()
	processlist2 = getProcessList()
	
	newProcesses = list()
	for x in pidlist2:
		if x not in pidlist1:
			newProcesses.append(x)
	print("After Process Termination")
	print(newProcesses)
	print("############")
	
	
	for x in newProcesses:
		for y in processlist2:
			if x in y:
				#os.kill(int(x),signal.SIGKILL)
				os.system("kill -9 {}".format(x))
				print("Killed " + x)
				print(x)
				print(y)
	pidlist2 = getAllPids()
	processlist2 = getProcessList()
	
	newProcesses = list()
	for x in pidlist2:
		if x not in pidlist1:
			newProcesses.append(x)
	print("After Process Termination")
	print(newProcesses)
	print("############")
	print("NOW WAITING....")
	time.sleep(10)
