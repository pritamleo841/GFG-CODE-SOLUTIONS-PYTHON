#User function Template for python3
from collections import deque,defaultdict
class Solution:
    def findSequences(self, startWord, targetWord, wordList):
        #BFS traversal (hard)
	    wordSet = set(wordList)  # Convert list to a set for O(1) lookups
        if targetWord not in wordSet:
            return []  # If endWord is not in the list, no transformation is possible
        
        queue = deque([[startWord]])  # BFS queue containing transformation sequences
        wordsUsedInLevel = set()  # Track words used in the current BFS level
        ans = []  # Stores final sequences
        found = False  # Flag to track if we reached endWord
        
        while queue:
            levelSize = len(queue)
            localUsed = set()  # Store words used in this level
            
            for _ in range(levelSize):
                path = queue.popleft()
                lastWord = path[-1]
                
                if lastWord == targetWord:
                    found = True
                    ans.append(path)  # Store valid transformation sequence
                
                for i in range(len(lastWord)):  # Try changing each letter
                    originalChar = lastWord[i]
                    
                    for c in 'abcdefghijklmnopqrstuvwxyz':  # Change to 'a' to 'z'
                        if c == originalChar:
                            continue
                        
                        newWord = lastWord[:i] + c + lastWord[i+1:]
                        
                        if newWord in wordSet:  # If transformation is valid
                            newPath = path + [newWord]  # Create new transformation sequence
                            queue.append(newPath)
                            localUsed.add(newWord)  # Mark word for removal after level
            
            if found:
                break  # Stop BFS once we find the shortest path
            
            wordSet -= localUsed  # Remove words used in this level
    
        return ans

#{ 
 # Driver Code Starts

from collections import deque 
import functools

def comp(a, b):
    x = ""
    y = ""
    for i in a:
        x += i 
    for i in b:
        y += i
    if x>y:
        return 1
    elif y>x:
        return -1 
    else:
        return 0

if __name__ == '__main__':
    T=int(input())
    for tt in range(T):
        n = int(input())
        wordList = []
        for i in range(n):
            wordList.append(input().strip())
        startWord = input().strip()
        targetWord = input().strip()
        obj = Solution()
        ans = obj.findSequences(startWord, targetWord, wordList)
        if len(ans)==0:
            print(-1)
        else:
            ans = sorted(ans, key=functools.cmp_to_key(comp))
            for i in range(len(ans)):
                for j in range(len(ans[i])):
                    print(ans[i][j],end=" ")
                print()

        print("~")
# } Driver Code Ends