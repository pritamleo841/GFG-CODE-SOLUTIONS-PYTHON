class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def Sorted(self, s):
        '''
        Sorting recursively means:
            1. Break the problem down by removing one element.
            2. Sort the smaller stack.
            3. Insert the removed element back in the correct position using a helper.
        '''
        def insert(stack,element):
            if not stack or stack[-1]<=element: #if top <=element or empty stack append
                stack.append(element)
            else:
                tmp = stack.pop() #extarct the top element
                insert(stack,element) #find suitable position to insert and append element
                stack.append(tmp) #append the extracted element at top
        if s:
            ele = s.pop()
            self.Sorted(s)
            insert(s,ele)
        



#{ 
 # Driver Code Starts

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.Sorted(arr)
        for e in range(len(arr)):
            print(arr.pop(), end=" ")
        print()


        print("~")
# } Driver Code Ends