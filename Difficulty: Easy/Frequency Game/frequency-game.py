#User function Template for python3
from collections import Counter
def LargButMinFreq(arr,n):
    freq = Counter(arr)
    min_freq = min(freq.values())
    max_val = float('-inf')
    for key,val in freq.items():
        if key>max_val and min_freq==val:
            max_val=key
    return max_val
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
#Iterating over test cases
for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(LargButMinFreq(arr, n))
    print("~")
# } Driver Code Ends