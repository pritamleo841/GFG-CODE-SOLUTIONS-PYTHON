from collections import defaultdict
class Solution:
    def subarrayXor(self, arr, k):
        #pair sum solution using map
        freq=defaultdict(int)
        xor=0
        count=0
        #a^b=c then a^c=b and b^c=a
        for elem in arr:
            xor=xor^elem
            if xor==k:
                count+=1
            if (xor^k) in freq:
                count+=freq[xor^k]
            freq[xor]+=1
        return count


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    tc = int(input())

    for _ in range(tc):
        arr = list(map(int, input().split()))
        k = int(input())

        obj = Solution()
        print(obj.subarrayXor(arr, k))
        print("~")

# } Driver Code Ends