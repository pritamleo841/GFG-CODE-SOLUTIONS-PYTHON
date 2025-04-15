#User function Template for python3
from functools import lru_cache
class Solution:
    def wordBreak(self, wordDict, s):
        '''
        1.We'll use recursion to try breaking the string at every possible index.
        2.If the prefix is a valid word (i.e., exists in the dictionary), we recursively break the rest of the string.
        3.We use memoization (lru_cache) to cache results for substrings and avoid recomputation.
        4.Finally, we collect all valid sentences and return them.
        '''
        word_set = set(wordDict)  # Fast lookup
        @lru_cache(None)
        
        def backtrack(start):
            if start == len(s):
                return [""]  # Base case: one valid way to end
    
            sentences = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    # Get rest of the sentences from `end` onwards
                    rest_sentences = backtrack(end)
                    for sentence in rest_sentences:
                        space = "" if sentence == "" else " "
                        sentences.append(word + space + sentence)
    
            return sentences
    
        return backtrack(0)


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        dicti = input().split()
        s = input()

        ob = Solution()
        ans = ob.wordBreak(dicti, s)
        if (len(ans) == 0):
            print("[]")
        else:
            ans.sort()
            for it in ans:
                print(it)
        print("~")
# } Driver Code Ends