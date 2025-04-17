#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3

class Solution:
    def heapify(self,arr,n,i):
        largest=i #Initialize largest as root
        left=2*i+1
        right=2*i+2
        #Check if left child exists and is greater than root
        if left<n and arr[left]>arr[largest]:
            largest=left
        #Check if right child exists and is greater than current largest
        if right<n and arr[right]>arr[largest]:
            largest=right
        #If largest is not root, swap and heapify
        if largest!=i:
            arr[i],arr[largest]=arr[largest],arr[i]
            self.heapify(arr,n,largest)
    
    def heapSort(self, arr):
        n=len(arr)
        #Build a max heap for descending order
        for i in range(n//2-1,-1,-1):
            self.heapify(arr,n,i)
        #Extract elements one by one
        for i in range(n-1,0,-1):
            #Swap current root to end
            arr[0],arr[i]=arr[i],arr[0]
            #Heapify reduced heap
            self.heapify(arr,i,0)
        return arr
            

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ob.heapSort(arr)
        print(*arr)
        print("~")
        t -= 1


# } Driver Code Ends