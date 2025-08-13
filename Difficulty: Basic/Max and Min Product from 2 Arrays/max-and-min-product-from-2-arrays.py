#User function Template for python3

class Solution:
    # Function to find the maximum element from array arr1 and 
    # the minimum element from array arr2 and return their product.
    def find_multiplication(self, arr1, arr2):
        n,m=len(arr1),len(arr2)
        if n==0 or m==0:
            return 0
        max_arr1=float('-inf')
        min_arr2=float('inf')
        for elem in arr1:
            max_arr1=max(max_arr1,elem)
        for elem in arr2:
            min_arr2=min(min_arr2,elem)
        return max_arr1*min_arr2
