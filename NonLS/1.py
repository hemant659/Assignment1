import sys
import numpy as np
import classifier
import CoVariance
import MatMult
import MatInverse
#import plot1
#import matplotlib
#matplotlib.use("Agg")
import matplotlib.pyplot as plt
m1=[]
m2=[]
p1=[]
p2=[]
q1=[]
q2=[]
mean_vector1=[]
mean_vector2=[]
sum1=sum2=0.00
fh=open("Class1Train.txt","r") 
for line in fh: 
	words=line.split()
	m1.append(float(words[0]))
	sum1=sum1+float(words[0])
	m2.append(float(words[1]))
	sum2=sum2+float(words[1])
	#plt.plot(float(words[0]),float(words[1]),'b')
	#print(words[0],words[1])
n1=len(m1)
plt.plot(m1,m2,'bo')
#plt.show()
mean_vector1.append(sum1/n1)
mean_vector2.append(sum2/n1)
#print(sum1,sum2,n1)
#print(mean_vector1[0],mean_vector2[0])
sum1=sum2=0.00
fi=open("Class2Train.txt","r") 
for line in fi: 
	words=line.split()
	p1.append(float(words[0]))
	sum1=sum1+float(words[0])
	p2.append(float(words[1]))
	sum2=sum2+float(words[1])
	#plt.plot(float(words[0]),float(words[1]),'b')
	#print(words[0],words[1])
plt.plot(p1,p2,'go')
#plt.show()
n2=len(p1)
mean_vector1.append(sum1/n2)
mean_vector2.append(sum2/n2)
#print(sum1,sum2,n2)
#print(mean_vector1[1],mean_vector2[1])
sum1=sum2=0.00
fj=open("Class3Train.txt","r") 
for line in fj: 
	words=line.split()
	q1.append(float(words[0]))
	sum1=sum1+float(words[0])
	q2.append(float(words[1]))
	sum2=sum2+float(words[1])
	#plt.plot(float(words[0]),float(words[1]),'b')
	#print(words[0],words[1])
n3=len(q1)
mean_vector1.append(sum1/n3)
mean_vector2.append(sum2/n3)
plt.plot(q1,q2,'ro')
plt.show()
"""print(sum1,sum2,n3)
print(mean_vector1[2],mean_vector2[2])
print("\n")"""

cov1 = [[0] * 2 for i in range(2)]
cov1_inv = [[0] * 2 for i in range(2)]
CoVariance.covariance(m1,m2,mean_vector1,mean_vector2,cov1,n1,0)
"""for i in range (0,2):
	for j in range (0,2):
		print(cov1[i][j])
print("\n")"""
cov1_inv = MatInverse.getMatrixInverse(cov1)
"""for i in range (0,2):
	for j in range (0,2):
		print(cov1_inv[i][j])
print("\n")"""

cov2 = [[0] * 2 for i in range(2)]
cov2_inv = [[0] * 2 for i in range(2)]
CoVariance.covariance(p1,p2,mean_vector1,mean_vector2,cov2,n2,1)
"""for i in range (0,2):
	for j in range (0,2):
		print(cov2[i][j])
print("\n")"""

cov2_inv = MatInverse.getMatrixInverse(cov2)
"""for i in range (0,2):
	for j in range (0,2):
		print(cov2_inv[i][j])
print("\n")"""


cov3 = [[0] * 2 for i in range(2)]
cov3_inv = [[0] * 2 for i in range(2)]
CoVariance.covariance(q1,q2,mean_vector1,mean_vector2,cov3,n3,2)
"""for i in range (0,2):
	for j in range (0,2):
		print(cov3[i][j])
print("\n")"""

cov3_inv = MatInverse.getMatrixInverse(cov3)
"""for i in range (0,2):
	for j in range (0,2):
		print(cov3_inv[i][j])
print("\n")"""

u1 = [[0] * 2 for i in range(1)]
u2 = [[0] * 1 for i in range(2)]
x = [[0] * 2 for i in range(1)]
y = [[0] * 1 for i in range(1)]
c1_x=np.zeros(1000000)
c2_x=np.zeros(1000000)
c3_x=np.zeros(1000000)
c1_y=np.zeros(1000000)
c2_y=np.zeros(1000000)
c3_y=np.zeros(1000000)
allx=[]
ally=[]
cl=[]
l1=0
l2=0
l3=0
u1 = [[0] * 2 for i in range(1)]
u2 = [[0] * 1 for i in range(2)]
for i in range (-120,120):
	for j in range (-120,120):
		px=(1.00*i)/20.00
		py=(1.00*j)/20.00
		u1[0][0]=px
		u1[0][1]=py
		allx.append(px)
		ally.append(py)
		color = classifier.assignClass1(u1,mean_vector1,mean_vector2,cov1,cov2,cov3)
		if color==1:
			c1_x[l1]=px
			c1_y[l1]=py
			l1+=1
		if color==2:
			c2_x[l2]=px
			c2_y[l2]=py
			l2+=1
		if color==3:
			c3_x[l3]=px
			c3_y[l3]=py
			l3+=1
		print(color)
#print(len(sys.argv))
#print(str(sys.argv[1]))
#plot1.plotsamples()
#plt.plot(allx,ally,'g')
#plt.show()
#plt.plot(c1_x,c1_y,'r')
#plt.show()
#plt.plot(c2_x,c2_y,'g')
#plt.show()

plt.plot(c3_x,c3_y,'#90EE90')
plt.plot(c2_x,c2_y,'#F08080')
plt.plot(c1_x,c1_y,'#00FFFF')
plt.plot(m1,m2,'bo')
plt.plot(p1,p2,'ro')
plt.plot(q1,q2,'go')
plt.show()
#plt.show()
print(len(m1),len(p1),len(q1))
count = classifier.assignClass(sys.argv[1],mean_vector1,mean_vector2,cov1,cov2,cov3)
print(l1,l2,l3)
print(count)
