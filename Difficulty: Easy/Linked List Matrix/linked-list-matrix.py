#User function Template for python3

'''

class Node():
    def __init__(self,x):
        self.data = x
        self.right = None
        self.down=None

'''

class Solution:
    def constructLinkedMatrix(self, mat):
        if not mat or not mat[0]:
            return None
        n=len(mat)
        head=None
        prev_row=[False]*n #keep track of raw previous nodes
        
        for i in range(n):
            row_head=None
            prev=None
            for j in range(n):
                new_node=Node(mat[i][j])
                #Set head if it's the first node
                if i==0 and j==0:
                    head=new_node
                #Link to previous node in the row
                if prev:
                    prev.right=new_node
                prev=new_node
                #Link to node above in the previous row
                if i>0:
                    prev_row[j].down=new_node
                #Update the current column in prev_row
                prev_row[j]=new_node
        return head
        
                
                    
        


#{ 
 # Driver Code Starts
class Node():

    def __init__(self, x):
        self.data = x
        self.right = None
        self.down = None


def display(head):
    Dp = head
    while Dp:
        Rp = Dp
        while Rp:
            print(Rp.data, end=" ")
            if Rp.right:
                print(Rp.right.data, end=" ")
            else:
                print("null", end=" ")
            if Rp.down:
                print(Rp.down.data, end=" ")
            else:
                print("null", end=" ")
            Rp = Rp.right
        Dp = Dp.down


if __name__ == "__main__":
    for _ in range(int(input())):
        # First row input
        a = list(map(int, input().strip().split()))
        n = len(a)

        # Input the matrix
        mat = [a]
        for i in range(1, n):
            row = list(map(int, input().strip().split()))
            mat.append(row)

        # Create a Solution object and construct the linked matrix
        obj = Solution()
        head = obj.constructLinkedMatrix(mat)
        if head is None:
            print(-1)
            continue
        display(head)
        print()
        print("~")

# } Driver Code Ends