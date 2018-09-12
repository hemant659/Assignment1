def transposeMatrix(m):
    return map(list,zip(*m))
def matrixMult(m1,m2):
    n=len(m1)
    m=len(m2[0])
    p=len(m2)
    #print(n,m,p)
    mat = [[0] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            mat[i][j]=0
    """for i in range(n):
        for j in range(m):
            print(mat[i][j])"""
    for i in range(n):
        for j in range(m):
            for k in range(p):
                mat[i][j]=mat[i][j]+(m1[i][k]*m2[k][j])
    return mat
