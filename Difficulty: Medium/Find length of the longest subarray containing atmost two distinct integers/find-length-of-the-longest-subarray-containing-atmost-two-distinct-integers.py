#User function Template for python3

class Solution:
    def totalElements(self,arr):
        #Find length of the longest subarray containing 
        #atmost two distinct integers
        from collections import Counter
        char_count = Counter()
        left=0
        max_len = 0
        start_idx = 0
        for right in range(len(arr)):
            char_count[arr[right]]+=1
            #if two distinct characters, shrink window
            while len(char_count)>2:
                char_count[arr[left]]-=1
                if char_count[arr[left]]==0:
                    del char_count[arr[left]]
                #left pointer increment
                left+=1
            if right-left+1>max_len:
                max_len=right-left+1
                start_idx = left
        #resultant subarray - arr[start_idx:start_idx+max_len]
        return max_len
                    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        # N = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.totalElements(arr)
        print(res)
        print("~")

# } Driver Code Ends