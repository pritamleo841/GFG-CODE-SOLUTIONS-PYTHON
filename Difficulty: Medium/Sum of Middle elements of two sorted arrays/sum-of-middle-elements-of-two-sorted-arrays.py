#User function Template for python3

class Solution:
    def sum_of_middle_elements(self, arr1, arr2):
        # code here
        #Using Binary Search Algo - O(logn)
        #Prerequisite - Median of two sorted arrays
        n=len(arr1)
        low,high=0,n
        
        while low<=high:
            mid1=(low+high)//2
            mid2=n-mid1 #For second array
            
            l1=arr1[mid1-1] if mid1>0 else float('-inf')
            l2=arr2[mid2-1] if mid2>0 else float('-inf')
            
            r1=arr1[mid1] if mid1<n else float('inf')
            r2=arr2[mid2] if mid2<n else float('inf')
            
            if l1<=r2 and l2<=r1 :
                return max(l1,l2)+min(r1,r2)
            elif l1>r2:
                high=mid1-1
            else:
                low=mid1+1
        return 0
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        #Brute force solution; TC:O(2n), SC:O(2n)
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