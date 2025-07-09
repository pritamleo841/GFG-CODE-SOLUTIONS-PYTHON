from collections import deque
class Solution:
	def FirstNonRepeating(self, s):
		'''
		1.For each character ch in the stream:
        2.Increment its count in a dictionary.
        3.Add it to the queue.
        4.While the front of the queue has a count>1 (i.e.repeated),pop it.
        5.If the queue is non-empty, the front is the first non-repeating char.
        6.Else, append #.
		'''
		count=[0]*26
        q=deque()
        result=[]
    
        for ch in s:
            idx=ord(ch)-ord('a')
            count[idx]+=1
            q.append(ch)
    
            while q and count[ord(q[0])-ord('a')] > 1:
                q.popleft()
    
            if q:
                result.append(q[0])
            else:
                result.append('#')
    
        return ''.join(result)