#User function Template for python3
class Solution:
    # Function to find values in array equal to their indices
    def valueEqualToIndex(self, arr):
        res=[]
        for i in range(len(arr)):
            if i==arr[i]-1:
                res.append(arr[i])
        return res
                