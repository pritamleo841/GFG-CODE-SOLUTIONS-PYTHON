#User function Template for python3


class Solution:

    def kthElement(self, a, b, k):
        
        
        n1,n2=len(a),len(b)
        if n1>n2:
            self.kthElement(b,a,k)
        n=n1+n2
        low,high=max(0,k-n2),min(k,n1)
        left=k
        
        while low<=high:
            l1,l2,r1,r2=float('-inf'),float('-inf'),float('inf'),float('inf')
            mid1=low+(high-low)//2
            mid2=left-mid1
            
            if mid1<n1:
                r1=a[mid1]
            if mid2<n2:
                r2=b[mid2]
            if mid1-1>=0:
                l1=a[mid1-1]
            if mid2-1>=0:
                l2=b[mid2-1]
            
            if l1<=r2 and l2<=r1:
                return max(l1,l2)
            elif l1>r2:
                high=mid1-1
            else:
                low=mid1+1
        return 0
            
        #Brute force solution
        #Use merge sort concept, store only the latest element
        #When k becomes 0,, just return the latest saved element
        # TC: O(n1+n2), SC: O(1)
        # i,j=0,0
        # n1,n2=len(a),len(b)
        # res=-1
        
        # while i<n1 and j<n2:
        #     if a[i]<b[j]:
        #         res=a[i]
        #         i+=1
        #         k-=1
        #     else :
        #         res=b[j]
        #         j+=1
        #         k-=1
                
        #     if k==0:
        #         return res
        
        # while i<n1:
        #     res=a[i]
        #     i+=1
        #     k-=1
            
        #     if k==0:
        #         return res
        # while j<n2:
        #     res=b[j]
        #     j+=1
        #     k-=1
            
        #     if k==0:
        #         return res
        # return res



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):

        k = int(input())
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement(a, b, k))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends