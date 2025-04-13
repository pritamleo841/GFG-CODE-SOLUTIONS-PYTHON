#User function Template for python3

class Solution:
    def isKPartitionPossible(self, arr, k):
        '''
        The idea is to:
            First check if the total sum of elements is divisible by k.
            If not, it's impossible.
            Use backtracking to try and assign each element to one of the k subsets,
            ensuring each subset reaches the target sum.
        '''
        total_sum=sum(arr)
        if total_sum%k!=0:
            return False
        target = total_sum//k
        used = [False]*len(arr)
        arr.sort(reverse=True) #to start with bigger numbers
        def backtrack(index,k,curr_sum):
            if k==1:
                return True
            if curr_sum==target:
                return backtrack(0,k-1,0)
            for i in range(index,len(arr)):
                if not used[i] and curr_sum+arr[i]<=target:
                    used[i]=True
                    if backtrack(i+1,k,curr_sum+arr[i]):
                        return True
                    used[i]=False
            return False
        return backtrack(0,k,0)
            

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tcs = int(input())
    for _ in range(tcs):
        arr = [int(x) for x in input().split()]
        k = int(input())
        if Solution().isKPartitionPossible(arr, k):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends