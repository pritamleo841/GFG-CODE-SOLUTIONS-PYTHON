# Your task is to complete this function
# Function to print postorder traversal
def printPost(inorder, preorder, inStart, inEnd, mp, preIndex):
    if inStart > inEnd:
        return
    # Find index of next item in preorder traversal in inorder
    inIndex=mp[preorder[preIndex[0]]]
    preIndex[0] += 1
    # Traverse left tree
    printPost(inorder,preorder,inStart,inIndex-1,mp,preIndex)
    # Traverse right tree
    printPost(inorder,preorder,inIndex+1,inEnd,mp,preIndex)
    # Print root node at the end of traversal
    print(inorder[inIndex],end=" ")

def printPostOrder(inorder, preorder):
    mp={val:idx for idx,val in enumerate(inorder)}
    # Use a list to hold the mutable index
    preIndex=[0]
    printPost(inorder,preorder,0,len(inorder)-1,mp, preIndex)



    
#{ 
 # Driver Code Starts
# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        ino = list(map(int, input().strip().split()))
        pre = list(map(int, input().strip().split()))
        printPostOrder(ino, pre)
        print('')
        print("~")
# contributed by: Harshit Sidhwa

# } Driver Code Ends