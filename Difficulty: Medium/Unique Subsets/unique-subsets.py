#User function Template for python3

class Solution:
    
    #Function to find all possible unique subsets.
    def AllSubsets(self, arr,n):
        result = []
        arr.sort() #to be explored in sorted order
        
        def backtrack(curr,index):
            result.append(curr[:])
            for i in range(index,len(arr)):
                if i>index and arr[i]==arr[i-1]: #skip duplicates
                    continue
                curr.append(arr[i]) #take current element
                backtrack(curr,i+1)
                curr.pop()          #do not take current element
        
        backtrack([],0)
        return result
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int,input().strip().split()))
        obj  = Solution()
        result = obj.AllSubsets(a,n)
        for i in range(len(result)):
            print("(",end="")
            size = len(result[i])
            for j in range(size-1):
                print(result[i][j],end=" ")
            if(size):
                print(result[i][size-1],end=")")
            else:
                print(")",end="")
        print()


        print("~")
# } Driver Code Ends