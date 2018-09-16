import sys
import numpy as np
import classifier
import CoVariance
import MatMult
import MatInverse
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
	#print(words[0],words[1])
n1=len(m1)
mean_vector1.append(sum1/n1)
mean_vector2.append(sum2/n1)
print(sum1,sum2,n1)
print(mean_vector1[0],mean_vector2[0])
sum1=sum2=0.00
fi=open("Class2Train.txt","r") 
for line in fi: 
	words=line.split()
	p1.append(float(words[0]))
	sum1=sum1+float(words[0])
	p2.append(float(words[1]))
	sum2=sum2+float(words[1])
	#print(words[0],words[1])
n2=len(p1)
mean_vector1.append(sum1/n2)
mean_vector2.append(sum2/n2)
print(sum1,sum2,n2)
print(mean_vector1[1],mean_vector2[1])
sum1=sum2=0.00
fj=open("Class3Train.txt","r") 
for line in fj: 
	words=line.split()
	q1.append(float(words[0]))
	sum1=sum1+float(words[0])
	q2.append(float(words[1]))
	sum2=sum2+float(words[1])
	#print(words[0],words[1])
n3=len(q1)
mean_vector1.append(sum1/n3)
mean_vector2.append(sum2/n3)
print(sum1,sum2,n3)
print(mean_vector1[2],mean_vector2[2])
print("\n")

cov1 = [[0] * 2 for i in range(2)]
cov1_inv = [[0] * 2 for i in range(2)]
CoVariance.covariance(m1,m2,mean_vector1,mean_vector2,cov1,n1,0)
for i in range (0,2):
	for j in range (0,2):
		print(cov1[i][j])
print("\n")
cov1_inv = MatInverse.getMatrixInverse(cov1)
for i in range (0,2):
	for j in range (0,2):
		print(cov1_inv[i][j])
print("\n")

cov2 = [[0] * 2 for i in range(2)]
cov2_inv = [[0] * 2 for i in range(2)]
CoVariance.covariance(p1,p2,mean_vector1,mean_vector2,cov2,n2,1)
for i in range (0,2):
	for j in range (0,2):
		print(cov2[i][j])
print("\n")

cov2_inv = MatInverse.getMatrixInverse(cov2)
for i in range (0,2):
	for j in range (0,2):
		print(cov2_inv[i][j])
print("\n")


cov3 = [[0] * 2 for i in range(2)]
cov3_inv = [[0] * 2 for i in range(2)]
CoVariance.covariance(q1,q2,mean_vector1,mean_vector2,cov3,n3,2)
for i in range (0,2):
	for j in range (0,2):
		print(cov3[i][j])
print("\n")

cov3_inv = MatInverse.getMatrixInverse(cov3)
for i in range (0,2):
	for j in range (0,2):
		print(cov3_inv[i][j])
print("\n")

u1 = [[0] * 2 for i in range(1)]
u2 = [[0] * 1 for i in range(2)]
x = [[0] * 2 for i in range(1)]
y = [[0] * 1 for i in range(1)]
prob1=[]
prob2=[]
prob3=[]
cl=[]
z=0
#print(len(sys.argv))
#print(str(sys.argv[1]))
count = classifier.assignClass(sys.argv[1],mean_vector1,mean_vector2,cov1,cov2,cov3)
print(count,z)