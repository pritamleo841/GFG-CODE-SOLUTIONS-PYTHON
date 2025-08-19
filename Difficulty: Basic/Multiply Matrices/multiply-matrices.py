# Your task is to complete this function
# function should store the multiplication in C
def multiply(a, b, c, n):
    for i in range(n):
        for j in range(n):
            c[i][j]=0
            for k in range(n):
                c[i][j]+=a[i][k]*b[k][j]
    return c