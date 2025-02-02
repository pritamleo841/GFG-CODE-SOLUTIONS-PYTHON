#User function Template for python3
from collections import deque
class Solution:
    def isCircle(self, arr):
        #BFS traversal to check for a circle
        n=len(arr)
        visited=[False]*n
        #Store incoming edges for the first char of a word
        indegree = [0]*26  
        #Store outgoing edges for the last char of a word
        outdegree = [0]*26  
        
        #Graph: Maps first character to list of word indices
        graph = {}  
        queue = deque()
        
        #Construct graph and degree arrays
        for i in range(n):
            first_char = ord(arr[i][0])-ord('a')
            last_char = ord(arr[i][-1])-ord('a')
            
            indegree[first_char] += 1
            outdegree[last_char] += 1
            
            if arr[i][0] not in graph:
                graph[arr[i][0]] = []
            graph[arr[i][0]].append(i)  # Append index of the word

        #Check if in-degree and out-degree match for all characters
        for key in graph:
            if indegree[ord(key)-ord('a')] != outdegree[ord(key)-ord('a')]:
                return 0

        # Step 3: Perform BFS to check connectivity
        queue.append(0)  # Start BFS from the first word
        visited[0] = True
        matches = 1
        
        while queue:
            index = queue.popleft()
            last_char = arr[index][-1]  # Last character of current word
            
            if last_char in graph:  # Ensure there are words that start with this letter
                for idx in graph[last_char]:  # Traverse words that start with last_char
                    if not visited[idx]:  
                        visited[idx] = True
                        queue.append(idx)
                        matches += 1
        
        # Step 4: Ensure all words are visited
        return 1 if matches == n else 0
            
        
        
        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(10**6)
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        A = input().split()

        ob = Solution()
        print(ob.isCircle(A))
        print("~")

# } Driver Code Ends