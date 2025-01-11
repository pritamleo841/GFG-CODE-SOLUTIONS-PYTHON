#User function Template for python3

class Solution:
    def sum_of_middle_elements(self, arr1, arr2):
        # code here
        #Brute force solution
        arr3=[]
        i,j=0,0
        n=len(arr1)
        while i<n and j<n:
            if arr1[i]<=arr2[j]:
                arr3.append(arr1[i])
                i+=1
            else:
                arr3.append(arr2[j])
                j+=1
        
        while i<n:
            arr3.append(arr1[i])
            i+=1
        while j<n:
            arr3.append(arr2[j])
            j+=1
        return arr3[n]+arr3[n-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

input = sys.stdin.read


def main():
    input_lines = input().strip().split("\n")
    t = int(input_lines[0])

    index = 1
    results = []
    while t > 0:
        arr = list(map(int, input_lines[index].strip().split()))
        brr = list(map(int, input_lines[index + 1].strip().split()))
        index += 2

        solution = Solution()
        res = solution.sum_of_middle_elements(arr, brr)
        results.append(res)

        t -= 1

    for result in results:
        print(result)
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends