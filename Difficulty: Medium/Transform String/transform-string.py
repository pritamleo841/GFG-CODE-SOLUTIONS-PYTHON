#Back-end complete function Template for Python 3
from collections import Counter
class Solution:
    def transform(self, A, B): 
        if len(A)!=len(B):
            return -1
        if Counter(A)!=Counter(B):
            return -1
        
        i,j=len(A)-1,len(B)-1
        counter=0
        while i>=0:
            if A[i]==B[j]:
                j-=1
            else:
                counter+=1
            i-=1
        return counter


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        line = input().strip().split()
        A = line[0]
        B = line[1]
        ob = Solution()
        print(ob.transform(A,B))
        print("~")
# } Driver Code Ends