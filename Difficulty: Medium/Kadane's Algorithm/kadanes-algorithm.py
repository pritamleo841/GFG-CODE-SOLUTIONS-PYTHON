class Solution:
    def maxSubArraySum(self, arr):
        # Your code here
        #Kadene's algorithm
        curr_sum = max_sum = arr[0]
        for i in range(1,len(arr)):
            curr_sum = max(arr[i],curr_sum+arr[i])
            max_sum = max(curr_sum,max_sum)
        return max_sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.maxSubArraySum(arr))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends