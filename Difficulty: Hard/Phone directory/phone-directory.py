#User function Template for python3
class TrieNode:
    def __init__(self):
        self.children={}
        self.words=set()
class Solution:
    #TC - O(n*m+L*logk)
    #where L is length of s and k is number of matched contacts
    def insert(self,root,word):
        node=root
        for char in word:
            if char not in node.children:
                node.children[char]=TrieNode()
            node=node.children[char]
            node.words.add(word)
            
    def prefixSearch(self,root,prefix):
        node=root
        for char in prefix:
            if char not in node.children:
                return ["0"]
            node=node.children[char]
        return sorted(node.words)
        
    def displayContacts(self, n, contact, s):
        contact=sorted(set(contact))
        root=TrieNode()
        for word in contact:
            self.insert(root,word)
        ans=[]
        for i in range(1,len(s)+1):
            prefix=s[:i]
            matches=self.prefixSearch(root,prefix)
            ans.append(matches)
        return ans
        
        '''
        #TC - O(nlogn)+O(L*(n*m+nlogn))
        ans = []
        contact = sorted(set(contact))  # remove duplicates and sort once
        for i in range(1,len(s)+1):
            prefix = s[:i]
            unique = set()
            for c in contact:
                if c.startswith(prefix):
                    unique.add(c)
            if not unique:
                temp = ["0"]
            else:
                temp = sorted(unique)
            ans.append(temp)
        return ans
        '''
                    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        contact = input().split()
        s = input()
        
        ob = Solution()
        ans = ob.displayContacts(n, contact, s)
        for i in range(len(s)):
            for val in ans[i]:
                print(val, end = " ")
            print()
        print("~")
# } Driver Code Ends