import CoVariance
import MatMult
import MatInverse
import numpy as np
import matplotlib
def assignClass(s,mean_vector1,mean_vector2,cov1,cov2,cov3):
	u1 = [[0] * 2 for i in range(1)]
	u2 = [[0] * 1 for i in range(2)]
	x = [[0] * 2 for i in range(1)]
	y = [[0] * 1 for i in range(1)]
	fo1=open(s,"r")
	z=0
	cl=[]
	cov1_inv = MatInverse.getMatrixInverse(cov1)
	cov2_inv = MatInverse.getMatrixInverse(cov2)
	cov3_inv = MatInverse.getMatrixInverse(cov3)
	for line in fo1: 
		z+=1
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
		#g1=g1+np.log(1.000/6.000)
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
		#g2=g2+(np.log(5.00/18.00));
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
		#g3=g3+(np.log(5.00/9));
		max1=max(max1,g3)
		if max1==g3 :
			max_idx=3
		#print(g1,g2,g3)
		cl.append(max_idx)
		#prob3.append(g)
		#max1=g1;
	count=0
	for i in range (0,z):
		if cl[i]==3 :
			count+=1
		#print(cl[i])
	#print(count,z)
	return count

def assignClass123(u1,mean_vector1,mean_vector2,cov1,cov2,cov3):
	u2 = [[0] * 1 for i in range(2)]
	x = [[0] * 2 for i in range(1)]
	y = [[0] * 1 for i in range(1)]
	z=0
	cl=[]
	cov1_inv = MatInverse.getMatrixInverse(cov1)
	cov2_inv = MatInverse.getMatrixInverse(cov2)
	cov3_inv = MatInverse.getMatrixInverse(cov3)
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
	g1=g1+np.log(1.000/6.000)
	max1=g1
	max_idx=1
	#prob1.append(g1)
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
	g2=g2+(np.log(5.00/18.00));
	max1=max(max1,g2)
	if max1==g2 :
		max_idx=2
	#prob2.append(g)
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
	g3=g3+(np.log(5.00/9));
	max1=max(max1,g3)
	if max1==g3 :
		max_idx=3
	return max_idx

def assignClass12(u1,mean_vector1,mean_vector2,cov1,cov2):
	u2 = [[0] * 1 for i in range(2)]
	x = [[0] * 2 for i in range(1)]
	y = [[0] * 1 for i in range(1)]
	z=0
	cl=[]
	cov1_inv = MatInverse.getMatrixInverse(cov1)
	cov2_inv = MatInverse.getMatrixInverse(cov2)
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
	#g1=g1+np.log(1.000/6.000)
	max1=g1
	max_idx=1
	#prob1.append(g1)
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
	#g2=g2+(np.log(5.00/18.00));
	max1=max(max1,g2)
	if max1==g2 :
		max_idx=2
	#prob2.append(g)
	return max_idx
def assignClass13(u1,mean_vector1,mean_vector2,cov1,cov3):
	u2 = [[0] * 1 for i in range(2)]
	x = [[0] * 2 for i in range(1)]
	y = [[0] * 1 for i in range(1)]
	z=0
	cl=[]
	cov1_inv = MatInverse.getMatrixInverse(cov1)
	cov3_inv = MatInverse.getMatrixInverse(cov3)
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
	#g1=g1+np.log(1.000/6.000)
	max1=g1
	max_idx=1
	#prob1.append(g1)
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
	#g2=g2+(np.log(5.00/18.00));
	max1=max(max1,g3)
	if max1==g3 :
		max_idx=3
	#prob2.append(g)
	return max_idx
def assignClass23(u1,mean_vector1,mean_vector2,cov2,cov3):
	u2 = [[0] * 1 for i in range(2)]
	x = [[0] * 2 for i in range(1)]
	y = [[0] * 1 for i in range(1)]
	z=0
	cl=[]
	cov2_inv = MatInverse.getMatrixInverse(cov2)
	cov3_inv = MatInverse.getMatrixInverse(cov3)
	u2[0][0]=u1[0][0]
	u2[1][0]=u1[0][1]
	x=MatMult.matrixMult(u1,cov2_inv)
	y=MatMult.matrixMult(x,u2)
	#print(y[0][0])
	g2=(-0.5000)*y[0][0]
	det=MatInverse.getMatrixDeternminant(cov2)
	if det<0:
		det=(-1.000)*det;
	sec=np.log(det)
	sec=(-0.500)*sec;
	g2=g2+sec;
	#g1=g1+np.log(1.000/6.000)
	max1=g2
	max_idx=2
	#prob1.append(g1)
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
	#g2=g2+(np.log(5.00/18.00));
	max1=max(max1,g3)
	if max1==g3 :
		max_idx=3
	#prob2.append(g)
	return max_idx