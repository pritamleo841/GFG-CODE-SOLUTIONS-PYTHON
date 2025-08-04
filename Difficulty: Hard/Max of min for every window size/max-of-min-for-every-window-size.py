
class Solution:
    def maxOfMins(self, arr):
        '''🔍 Key Idea:
        For each element in the array:
        Determine the maximum window size in which this element is the minimum.
        For each window size k, find the maximum among all the elements that can be minimum in a window of size k.
        
        ✅ Steps:
        For each element arr[i], find:
            prev_smaller[i]: index of previous smaller element on the left.
            next_smaller[i]: index of next smaller element on the right.
        
        From this, you know the window size in which arr[i] is the minimum.
        Build an array res[] of size n + 1 (1-based index), where res[k] keeps track of the maximum of minimums for window size k.
        Traverse res[] from right to left and fill empty entries to ensure all window sizes have correct values.
        '''
        n = len(arr)
        res = [0] * (n + 1)
        stack = []
    
        # Arrays to store previous and next smaller element indices
        prev_smaller = [-1] * n
        next_smaller = [n] * n
    
        # Find previous smaller for each element
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                prev_smaller[i] = stack[-1]
            stack.append(i)
    
        # Clear stack to reuse it
        stack.clear()
    
        # Find next smaller for each element
        for i in reversed(range(n)):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                next_smaller[i] = stack[-1]
            stack.append(i)
    
        # Fill res[] with max of minimums for each window length
        for i in range(n):
            # Length of the window in which arr[i] is minimum
            length = next_smaller[i] - prev_smaller[i] - 1
            res[length] = max(res[length], arr[i])
    
        # Fill empty entries (important step)
        for i in range(n - 1, 0, -1):
            res[i] = max(res[i], res[i + 1])
    
        return res[1:]  # Skip index 0
        
