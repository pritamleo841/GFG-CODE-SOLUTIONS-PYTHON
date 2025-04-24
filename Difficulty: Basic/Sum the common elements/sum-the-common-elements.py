#User function Template for python3
class Solution:
    def commonSum(self,n1,n2,arr1,arr2):
        MOD = 10**9 + 7
    
        # Step 1: Convert both arrays to sets to remove duplicates
        set1 = set(arr1)
        set2 = set(arr2)
        
        # Step 2: Find the intersection of both sets (common unique elements)
        common_elements = set1.intersection(set2)
        
        # Step 3: Sum the common elements
        result = sum(common_elements) % MOD
        
        # Step 4: Return the result
        return result
                


#{ 
 # Driver Code Starts

if __name__ == '__main__':
    for _ in range(int(input())):
        n1,n2 = map(int,input().split())
        arr1 = list(map(int,input().split()))
        arr2 = list(map(int,input().split()))
        obj = Solution()
        print(obj.commonSum(n1,n2,arr1,arr2))

        print("~")
# } Driver Code Ends