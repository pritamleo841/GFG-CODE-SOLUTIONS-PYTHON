from collections import deque
class Solution:
	def wordLadderLength(self, startWord, targetWord, wordList):
		#BFS traversal
		words = set()
		for item in wordList:
		    words.add(item)
		    
		queue=deque()
		queue.append((startWord,1)) #word generated,steps to reach
		#if already visited, remove from set(similar as visited[i][j]=False)
		if startWord in words:
		    words.remove(startWord)
		    
		while queue:
		    word,level = queue.popleft()
		    if word == targetWord:
		        return level
		    #replace each index character with ['a'-'z']
		    for i in range(len(word)):
		        originalChar = word[i]
		        for ch in 'abcdefghijklmnopqrstuvwxyz':
		            if ch == originalChar:
		                continue
		            #construct new word and check in the set
		            newWord = word[:i]+ch+word[i+1:]
		            if newWord in words:
		                queue.append((newWord,level+1))
		                words.remove(newWord)
		return 0
		            
		        
		


#{ 
 # Driver Code Starts
# from collections import deque
if __name__ == '__main__':
    T = int(input())
    for tt in range(T):
        n = int(input())
        wordList = []
        for i in range(n):
            wordList.append(input().strip())
        startWord = input().strip()
        targetWord = input().strip()
        obj = Solution()
        ans = obj.wordLadderLength(startWord, targetWord, wordList)
        print(ans)
        print("~")

# } Driver Code Ends