# User function Template for python3
from collections import defaultdict
class Solution:
    def longestSubarray(self, arr, k):  
        freq=dict()
        curr_sum=0
        max_length=0
        for i in range(len(arr)):
            curr_sum+=arr[i]
            if curr_sum==k:
                max_length=i+1
            #If curr_sum-k is found earlier at index j,
            #then subarray from j+1 to i sums to k,and its length is i-j.
            elif (curr_sum-k) in freq:
                max_length=max(max_length,i-freq[curr_sum-k])
            #stores the first occurrence index of a given prefix sum
            if curr_sum not in freq:
                freq[curr_sum]=i
        return max_length
            
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        print(ob.longestSubarray(arr, k))
        tc -= 1
        print("~")
# } Driver Code Ends