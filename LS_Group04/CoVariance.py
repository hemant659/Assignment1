def covariance(m1,m2,mean_vector,cov,n):
	diff = [[0] * 2 for i in range(n)]
	for i in range (0,n):
		diff[i][0]=m1[i]-mean_vector[0]
		diff[i][1]=m2[i]-mean_vector[1]
	for i in range (0,2):
		for j in range (0,2):
			sum=0
			for k in range (0,n):
				sum=sum+(diff[k][i]*diff[k][j])
			cov[i][j]=sum/n-1
