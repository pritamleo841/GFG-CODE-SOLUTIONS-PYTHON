#User function Template for python3
class Solution:
    def kLevelSumRecur(self,i, s, k, level):
        if s[i[0]] == '(':
            i[0] += 1
        # Find the value of current node.
        val = 0
        while i[0] < len(s) and s[i[0]] != '(' and s[i[0]] != ')':
            val=val*10+(ord(s[i[0]])-ord('0'))
            i[0]+= 1
        # Append the value of current node
        # only if it is at level k.
        val = val if level == k else 0
        left, right = 0, 0
        # If left subtree exists
        if i[0]<len(s) and s[i[0]]=='(':
            left=self.kLevelSumRecur(i, s, k, level + 1)
        # if right subtree exists
        if i[0]<len(s) and s[i[0]]=='(':
            right=self.kLevelSumRecur(i, s, k, level + 1)
        # To take care of closing parenthesis
        i[0]+= 1
        return val+left+right

    def kLevelSum(self, s, k):
        i = [0]
        return self.kLevelSumRecur(i, s, k, 0)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        k = int(input())
        ob = Solution()
        print(ob.kLevelSum(s, k))
        print("~")

# } Driver Code Ends