

class Solution:
    
    #Function to find the minimum number of swaps required to sort the array.
	def minSwaps(self, arr):
		#Code here
		n=len(arr)
		# Step 1: Pair elements with their indices and sort
		#avoid using enumerate
		arr_pos = []
        for index in range(n):
            arr_pos.append((arr[index], index))
		    
		arr_pos.sort(key=lambda x : x[0])
		
		# Step 2: Initialize visited array
		visited = [False]*n
		swaps=0
		
		# Step 3: Traverse the array and find cycles
		for i in range(n):
		    #If the element is already visited or in the correct position, skip
		    if visited[i] or arr_pos[i][1]==i:
		        continue
		    # Find the cycle
		    cycle_length=0
		    j=i
		    while not visited[j]:
		        visited[j]=True
		        # Move to the index of the next element in the cycle
		        j = arr_pos[j][1]
		        cycle_length+=1
		    #If there is a cycle, add (cycle_length - 1) to the swaps count   
		    if cycle_length>1:
		        swaps+=(cycle_length-1)
		    
		return swaps
		        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.minSwaps(arr)
        print(res)
        t -= 1
# } Driver Code Ends