import CoVariance
import MatMult
import MatInverse
fh=open("Class1.txt","r") 
m1=[]
m2=[]
sum1=sum2=0.00
for line in fh: 
	words=line.split()
	m1.append(float(words[0]))
	sum1=sum1+float(words[0])
	m2.append(float(words[1]))
	sum2=sum2+float(words[1])
	#print(words[0],words[1])
n=len(m1)
i=0
"""for i in range (0,n):
	print(m1[i],m2[i])"""
mean_vector=[]
print(sum1,sum2,n)
mean_vector.append(sum1/n)
mean_vector.append(sum2/n)
print(mean_vector[0],mean_vector[1])
#diff = [[0] * 2 for i in range(n)]
cov = [[0] * 2 for i in range(2)]
cov1_inv = [[0] * 2 for i in range(2)]
"""for i in range (0,n):
	diff[i][0]=m1[i]-mean_vector[0]
	diff[i][1]=m2[i]-mean_vector[1]
for i in range (0,n):
	print(diff[i][0],diff[i][1])"""
"""for i in range (0,2):
	for j in range (0,2):
		sum=0
		for k in range (0,n):
			sum=sum+(diff[k][i]*diff[k][j])
		cov[(m1,m2,mean_vector,)i][j]=sum/n-1"""
CoVariance.covariance(m1,m2,mean_vector,cov,n)
for i in range (0,2):
	for j in range (0,2):
		print(cov[i][j])
cov1_inv = MatInverse.getMatrixInverse(cov)
for i in range (0,2):
	for j in range (0,2):
		print(cov1_inv[i][j])
a, b = map(float, input().split())
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
		print(z[i][j])
#still lot of work to do