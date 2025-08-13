#User function Template for python3
import heapq
class Solution:
    def sortedMatrix(self,n,mat):
        temp=[]
        for i in range(n):
           for j in range(n):
                temp.append(mat[i][j])
        temp.sort()
        k=0
        for i in range(n):
            for j in range(n):
                mat[i][j]=temp[k]
                k+=1
        return mat