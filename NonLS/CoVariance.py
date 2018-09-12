def covariance(m1,m2,mean_vector1,mean_vector2,cov,n,file_idx):
	diff = [[0] * 2 for i in range(n)]
	#print("testing",m1[499],m2[499],"\n")
	for i in range (0,n):
		diff[i][0]=m1[i]-mean_vector1[file_idx]
		diff[i][1]=m2[i]-mean_vector2[file_idx]
	for i in range (0,2):
		for j in range (0,2):
			sum=0
			for k in range (0,n):
				sum=sum+(diff[k][i]*diff[k][j])
			cov[i][j]=sum/n
