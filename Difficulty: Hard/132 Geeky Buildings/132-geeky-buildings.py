#User function Template for python3

class Solution:
	def recreationalSpot(self, arr, n):
	    '''
	    O(N) solution using monotonic stack -
	    
	    We will iterate from the end and keep track of potential candidates 
	    for the third building (arr[k]) using a stack. 
	    We also maintain a variable to track the maximum possible value 
	    for arr[k] (the "2" in the 132 pattern).
	    '''
	    if n < 3:
            return False
        stack = []
        third = float('-inf')  # This will hold the potential "2" in the 132 pattern
        # Traverse from the end to the beginning
        for i in range(n - 1, -1, -1):
            if arr[i] < third:
                # Found a valid triplet: arr[i] < third < something on stack (arr[j])
                return True
            while stack and arr[i] > stack[-1]:
                # Pop from stack and update 'third'
                third = stack.pop()
            stack.append(arr[i])
    
        return False
	    
		'''
		O(N^2) solution
		1.We iterate the middle element j from 1 to N-2 and:
        2.Find minLeft = minimum to the left of j (arr[0] to arr[j-1])
        3.For each k from j+1 to N-1, if arr[k] > minLeft and arr[k] < arr[j], then return True
	
        if n < 3:
            return False
        # Precompute the minimum to the left of each index
        min_left = [0] * n
        min_left[0] = arr[0]
        for i in range(1, n):
            min_left[i] = min(min_left[i - 1], arr[i])
    
        # Try every middle element
        for j in range(1, n - 1):
            for k in range(j + 1, n):
                if min_left[j - 1] < arr[k] < arr[j]:
                    return True
        return False
        '''