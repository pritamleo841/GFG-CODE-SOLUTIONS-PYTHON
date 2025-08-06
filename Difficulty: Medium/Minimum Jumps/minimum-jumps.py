class Solution:
	def minJumps(self, arr):
	    '''
	    #Greedy Algorithm:-
	    
	    We keep track of:
            jumps: How many jumps we've used
            maxReach: The farthest index we can reach from any position so far
            steps: Steps we can still take in the current jump
	    '''
	    n=len(arr)
	    if n<=1:
	        return 0
	    if arr[0]==0:
	        return -1
	    jumps=1
	    max_reach=steps=arr[0]
	    for i in range(1,n):
	        if i==n-1:
	            return jumps
	        max_reach=max(max_reach,arr[i]+i)
	        steps-=1
	        if steps==0:
	            jumps+=1
	            if i>=max_reach:
	                return -1
	            steps=max_reach-i
	    return -1
	        
	    
	    
	    