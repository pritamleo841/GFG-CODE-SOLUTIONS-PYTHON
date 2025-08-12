#User function Template for python3

class Solution:
    def shortestUnorderedSubarray(self, arr):
        '''
        It’s about finding the smallest subarray which is not strictly increasing or not strictly decreasing.
        If the whole array is strictly increasing or strictly decreasing → shortest unordered subarray length = 0
        Else, the shortest unordered subarray will always be 3 (because with 2 elements, it’s either increasing or decreasing).

        Reasoning
        In a strictly increasing or strictly decreasing array, every subarray of length ≤ 2 is ordered.
        For any unordered array, there must exist three consecutive elements where the middle one breaks the order.
        So if the array is not entirely increasing or decreasing, answer is 3.
        '''
        n=len(arr)
        # Check if strictly increasing
        inc=all(arr[i]<arr[i+1] for i in range(n-1))
        # Check if strictly decreasing
        dec=all(arr[i]>arr[i+1] for i in range(n-1))
        
        if inc or dec:
            return 0
        return 3
    
    