#{ 
 # Driver Code Starts
import sys
sys.setrecursionlimit(10008)


# } Driver Code Ends

#User function Template for python3
class Solution:
    def deleteMid(self, stack):
        size=len(stack)
        def recur(stack,count):
            if count==size//2:
                stack.pop()
                return
            tmp=stack.pop()
            recur(stack,count+1)
            #after middle element is deleted, push elements onto the stack
            stack.append(tmp)
        recur(stack,0)
                
            

#{ 
 # Driver Code Starts.


if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        line = input().strip()
        stack = list(map(int, line.split()))

        # Reverse the list to mimic stack behavior (LIFO)

        ob = Solution()
        ob.deleteMid(stack)

        # Reverse again to print in expected order
        stack.reverse()
        print(" ".join(map(str, stack)))
        print("~")

# } Driver Code Ends