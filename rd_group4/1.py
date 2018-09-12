import numpy as np
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

v1=[]
v2=[]
w1=[]
w2=[]
u1 = [[0] * 2 for i in range(1)]
u2 = [[0] * 1 for i in range(2)]
x = [[0] * 2 for i in range(1)]
y = [[0] * 1 for i in range(1)]
prob1=[]
prob2=[]
prob3=[]
cl=[]
fo1=open("Class3Test.txt","r")
for line in fo1: 
	words=line.split()
	u1[0][0]=(float(words[0])-mean_vector1[0])
	u1[0][1]=(float(words[1])-mean_vector2[0])
	u2[0][0]=u1[0][0]
	u2[1][0]=u1[0][1]
	x=MatMult.matrixMult(u1,cov1_inv)
	y=MatMult.matrixMult(x,u2)
	#print(y[0][0])
	g1=(-0.5000)*y[0][0]
	det=MatInverse.getMatrixDeternminant(cov1)
	if det<0:
		det=(-1.000)*det;
	sec=np.log(det)
	sec=(-0.500)*sec;
	g1=g1+sec;
	g1=g1+np.log(0.3534)
	max1=g1
	max_idx=1
	#prob1.append(g1)

	u1[0][0]=(float(words[0])-mean_vector1[1])
	u1[0][1]=(float(words[1])-mean_vector2[1])
	u2[0][0]=u1[0][0]
	u2[1][0]=u1[0][1]
	x=MatMult.matrixMult(u1,cov2_inv)
	y=MatMult.matrixMult(x,u2)
	#print(y[0][0])
	g2=(-0.5000)*y[0][0]
	det=MatInverse.getMatrixDeternminant(cov2)
	if det<0 :
		det=(-1.000)*det;
	sec=np.log(det)
	sec=(-0.500)*sec;
	g2=g2+sec;
	g2=g2+(np.log(0.307));
	max1=max(max1,g2)
	if max1==g2 :
		max_idx=2
	#prob2.append(g)

	u1[0][0]=(float(words[0])-mean_vector1[2])
	u1[0][1]=(float(words[1])-mean_vector2[2])
	u2[0][0]=u1[0][0]
	u2[1][0]=u1[0][1]
	x=MatMult.matrixMult(u1,cov3_inv)
	y=MatMult.matrixMult(x,u2)
	#print(y[0][0])
	g3=(-0.5000)*y[0][0]
	det=MatInverse.getMatrixDeternminant(cov3)
	if det<0 :
		det=(-1.000)*det;
	sec=np.log(det)
	sec=(-0.500)*sec;
	g3=g3+sec;
	g3=g3+(np.log(0.3392));
	max1=max(max1,g3)
	if max1==g3 :
		max_idx=3
	print(g1,g2,g3)
	cl.append(max_idx)
	#prob3.append(g)
	#max1=g1;
count=0
for i in range (0,597):
	if cl[i]==3 :
		count+=1
	#print(cl[i])
print(count)
"""a, b = map(float, input().split())
x=[[0] * 2 for i in range(1)]
x[0][0]=a
x[0][1]=b
print(x[0][0],x[0][1])
#y=MatMult.transposeMatrix(x)
y = [[0] * 1 for i in range(2)]
z = [[0] * 2 for i in range(1)]
z=MatMult.matrixMult(x,cov1_inv)
for i in range (len(z)):
	for j in range (len(z[0])):
		print(z[i][j])"""
#still lot of work to do