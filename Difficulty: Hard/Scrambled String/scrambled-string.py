#User function Template for python3

class Solution:
    def isScramble(self,s1: str, s2: str, memo={}):
        '''
        Split s1 into two substrings and compare with corresponding parts of s2 in two possible ways:
        Without swapping: Check if the first part of s1 matches the first part of s2, and the second part of s1 matches the second part of s2.
        With swapping: Check if the first part of s1 matches the last part of s2, and vice versa.
        
        We use a dictionary (memo) to store previously computed results to optimize performance.
        '''
        if (s1, s2) in memo:
            return memo[(s1, s2)]
    
        if s1 == s2:
            return True
        
        if sorted(s1) != sorted(s2):  # Quick check to eliminate impossible cases
            return False
    
        n = len(s1)
        for i in range(1, n):
            # Case 1: No swap
            if self.isScramble(s1[:i], s2[:i], memo) and self.isScramble(s1[i:], s2[i:], memo):
                memo[(s1, s2)] = True
                return True
            # Case 2: Swap happens
            if self.isScramble(s1[:i], s2[-i:], memo) and self.isScramble(s1[i:], s2[:-i], memo):
                memo[(s1, s2)] = True
                return True
    
        memo[(s1, s2)] = False
        return False



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        S1,S2=input().split()
        if(Solution().isScramble( S1 , S2)):
            print("Yes")
        
        else:
            print("No")


        print("~")
# } Driver Code Ends