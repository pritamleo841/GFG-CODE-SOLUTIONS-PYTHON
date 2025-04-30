#User function Template for python3
from collections import defaultdict
class Solution:
    def longestKSubstr(self, s, k):
        #sliding window + hash map
        #similar as maximum substring with atmost k unique characters
        freq=defaultdict(int)
        n=len(s)
        if n==0 or k==0:
            return -1
        left=0
        max_len=-1
        freq=defaultdict(int)
        for right in range(n):
            freq[s[right]]+=1
            #If more than k unique characters, shrink from left
            while len(freq)>k:
                freq[s[left]]-=1
                if freq[s[left]]==0:
                    del freq[s[left]]
                left+=1
             #If exactly k unique characters, update max length
            if len(freq)==k:
                 max_len=max(max_len,right-left+1)
        return max_len

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()
        k = int(input())

        solObj = Solution()

        ans = solObj.longestKSubstr(s, k)

        print(ans)

        print("~")
# } Driver Code Ends