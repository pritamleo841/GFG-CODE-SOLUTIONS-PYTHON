class Solution:
    def maxSubArraySum(self, arr):
        # Your code here
        #Kadene's algorithm
        curr_sum=max_sum=arr[0]
        start=end=s=0  # Pointers to track the subarray
    
        for i in range(1,len(arr)):
            if arr[i]>curr_sum+arr[i]:  # Start new subarray
                curr_sum=arr[i]
                s=i  # Update starting index
            else:
                curr_sum+=arr[i]  # Extend current subarray
            
            if curr_sum>max_sum:  # Update max sum and subarray indices
                max_sum=curr_sum
                start=s
                end=i
        #arr[start:end+1] =>maximum subarray sum subarray
        return max_sum  # Return max sum
        '''
        #Kadene's algorithm
        curr_sum = max_sum = arr[0]
        for i in range(1,len(arr)):
            curr_sum = max(arr[i],curr_sum+arr[i])
            max_sum = max(curr_sum,max_sum)
        return max_sum
        '''


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