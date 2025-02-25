
class Solution:
    def isMaxHeap(self,arr,n):
        #check if a parent is greater than its left and right child
        for i in range(n//2):
            left_child = 2*i+1
            right_child = 2*i+2
            
            if left_child<n and arr[i]<arr[left_child]:
                return False
            if right_child<n and arr[i]<arr[right_child]:
                return False
        return True


#{ 
 # Driver Code Starts
if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]
        ob=Solution()
        print(int(ob.isMaxHeap(arr,n)))
        print("~")
# } Driver Code Ends