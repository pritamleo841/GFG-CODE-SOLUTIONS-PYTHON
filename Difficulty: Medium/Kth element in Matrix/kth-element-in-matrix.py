#User function Template for python3
import heapq
def kthSmallest(mat, n, k): 
    minHeap=[]
    for r in range(n):
        for c in range(n):
            heapq.heappush(minHeap,mat[r][c])
    res=0
    while k:
        res=heapq.heappop(minHeap)
        k-=1
    return res




#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Driver Code 

def main():
    T=int(input())
    while(T>0):
        n = int(input())
        mat=[[0 for j in range(n)] for i in range(n)]
        line1=[int(x) for x in input().strip().split()]
        k = int(input())

        temp=0
        for i in range(n):
            for j in range (n):
                mat[i][j]=line1[temp]
                temp+=1
        
        print(kthSmallest(mat, n, k))
        T-=1


        print("~")
if __name__=="__main__":
    main()




# } Driver Code Ends