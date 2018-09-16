import CoVariance
import MatMult
import MatInverse
import numpy as np
import matplotlib.pyplot as plt
import Class1Train.txt
def plotsamples():
	fo1=open(Class1Train.txt,"r")
	for line in fo1: 
		words=line.split()
		plt.plot(float(words[0]),float(words[1]))
	fo2=open(Class2Train.txt,"r")
	for line in fo2: 
		words=line.split()
		plt.plot(float(words[0]),float(words[1]))
	fo3=open(Class3Train.txt,"r")
	for line in fo3: 
		words=line.split()
		plt.plot(float(words[0]),float(words[1]))
	plt.show()