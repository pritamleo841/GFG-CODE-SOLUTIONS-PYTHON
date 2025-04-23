#User function Template for python3
class Node:
    def __init__(self,freq,char,index):
        self.freq=freq
        self.char=char
        self.index=index
        self.left=None
        self.right=None
    #Custom comparator for priority queue
    def __lt__(self,other):
        #If two nodes have the same value,
        #the one which occurs first goes to the left.
        # if self.freq==other.freq:
        #     return self.index<other.index
        #If frequencies are different, 
        #it orders them by ascending frequency
        return self.freq<other.freq
import heapq
class Solution:
    def huffmanCodes(self,S,f,N):
        min_heap = []
        for i in range(N):
            heapq.heappush(min_heap,Node(f[i],S[i],i)) #freq,chr,index
        
        count=N
        while len(min_heap)>1:
            left=heapq.heappop(min_heap)
            right=heapq.heappop(min_heap)
            
            new_node=Node(left.freq+right.freq,'#',count)
            new_node.left=left
            new_node.right=right
            heapq.heappush(min_heap,new_node)
            count+=1
        
        root=heapq.heappop(min_heap)
        result=[]
        def preorder(node,code):
            if not node:
                return None
            if node.char!='#':
                result.append(code)
            preorder(node.left,code+'0')
            preorder(node.right,code+'1')
        preorder(root,'')
        return result
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S= input()
		N= len(S);
		f= [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.huffmanCodes(S,f,N)
		for i in ans:
		    print(i, end = " ")
		print()
# } Driver Code Ends