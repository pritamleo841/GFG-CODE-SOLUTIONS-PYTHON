class Solution:
    def shuffleArray(self, arr, n):
        #use bitwise manipulation
        mid=n//2  # Correcting n to be the midpoint

        # Store two values in one variable using bitwise encoding
        for i in range(mid):  
            arr[i] = (arr[i]<<10) | arr[i+mid]  # Combine arr[i] and arr[mid + i]
        
        k=2*mid-1  # Last index in interleaved array
        for i in range(mid-1,-1,-1):
            y = arr[i] & ((1<<10)-1)  # Extract second half element
            x = arr[i]>>10  # Extract first half element
            arr[k] = y  # Place y at the correct position
            arr[k-1] = x  # Place x at the correct position
            k-=2
        
        return arr
        
        '''
        Accepted solution but using insert() method-
        
        mid=n//2  # Midpoint of the array
        i,j=1,mid  # Start from second element and midpoint
    
        while i<n and j<n:
            arr.insert(i,arr.pop(j))  # Insert stored element at correct position
            i += 2  # Move to next odd position
            j += 1  # Move to next element in second half
        return arr
        '''
            
            


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