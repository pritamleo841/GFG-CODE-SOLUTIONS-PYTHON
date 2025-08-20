class Solution:
    def check_elements(self, arr, n, A, B):
        # Your code goes here
        s=set(arr)   # for quick lookup
        for num in range(A,B+1):
            if num not in s:
                return False
        return True