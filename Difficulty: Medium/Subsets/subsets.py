#User function Template for python3

class Solution:
    def subsets(self, arr):
        res = []
        def backtrack(index,subset):
           res.append(subset[:])
           for i in range(index,len(arr)):
                subset.append(arr[i])
                backtrack(i+1,subset)
                subset.pop()
        backtrack(0,[])
        return res

#{ 
 # Driver Code Starts
# Example to simulate input/output behavior:
if __name__ == "__main__":
    t = int(input())  # Number of test cases
    for _ in range(t):
        arr = list(map(int,
                       input().split())
                   )  # Reading the array input as space-separated integers

        ob = Solution()
        res = ob.subsets(arr)

        # Print result
        for subset in res:
            if len(subset) == 0:
                print("[]")
            else:
                for num in subset:
                    print(num, end=" ")
                print()

        print("~")

# } Driver Code Ends