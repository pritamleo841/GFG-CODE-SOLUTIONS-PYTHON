#User function Template for python3
class Solution:
	def bracketNumbers(self, string):
		stack=[]
		count=1
		ans=[]
		for elem in string:
		    if elem=='(':
		        stack.append(count)
		        ans.append(count)
		        count+=1
		    elif elem==')':
		        ans.append(stack.pop())
		return ans
		    