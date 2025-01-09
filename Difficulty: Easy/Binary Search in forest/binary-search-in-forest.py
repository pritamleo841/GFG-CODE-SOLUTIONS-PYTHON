class Solution:
    def findCut(self,tree,mid,n):
        sum=0
        for i in range(n-1,-1,-1):
            if tree[i]-mid <=0 :
                break
            sum+=tree[i]-mid
        return sum
        
    def find_height(self,tree,n,k):
        # code here
        tree = sorted(tree)
        low = 0
        high = tree[n-1]
        
        while low<=high :
            mid=low+(high-low)//2
            minCut = self.findCut(tree,mid,n)
            if minCut == k:
                return mid
            elif minCut > k:
                low=mid+1
            else:
                high=mid-1
        return -1
            
        
        


#{ 
 # Driver Code Starts

t = int(input())
for _ in range(t):
    n = int(input())
    tree = [ int(x) for x in input().strip().split() ]
    k = int(input())
    ob=Solution()
    print(ob.find_height(tree,n,k))
    print("~")
# } Driver Code Ends