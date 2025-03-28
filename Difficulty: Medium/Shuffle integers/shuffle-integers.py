class Solution:
    def shuffleArray(self, arr, n):
        mid=n//2  # Midpoint of the array
        i,j=1,mid  # Start from second element and midpoint
    
        while i<n and j<n:
            arr.insert(i,arr.pop(j))  # Insert stored element at correct position
            i += 2  # Move to next odd position
            j += 1  # Move to next element in second half
        return arr
            
            


#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    t=int(input())
    for _ in range(0,t):
        n=int(input())
        a = list(map(int,input().split()))
        ob = Solution()
        ob.shuffleArray(a,n)
        print(*a)
# } Driver Code Ends