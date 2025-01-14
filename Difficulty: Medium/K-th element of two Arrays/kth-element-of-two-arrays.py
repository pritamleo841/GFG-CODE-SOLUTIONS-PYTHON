#User function Template for python3


class Solution:

    def kthElement(self, a, b, k):
        
        
        
        #Brute force solution
        #Use merge sort concept, store only the latest element
        #When k becomes 0,, just return the latest saved element
        # TC: O(n1+n2), SC: O(1)
        i,j=0,0
        n1,n2=len(a),len(b)
        res=-1
        
        while i<n1 and j<n2:
            if a[i]<b[j]:
                res=a[i]
                i+=1
                k-=1
            else :
                res=b[j]
                j+=1
                k-=1
                
            if k==0:
                return res
        
        while i<n1:
            res=a[i]
            i+=1
            k-=1
            
            if k==0:
                return res
        while j<n2:
            res=b[j]
            j+=1
            k-=1
            
            if k==0:
                return res
        return res



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