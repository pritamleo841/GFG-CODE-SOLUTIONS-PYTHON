#User function Template for python3
import math as m
from collections import defaultdict
class Solution:
    def countFractions(self, n, numerator, denominator):
        counter=0
        fraction_map = defaultdict(int)
        for i in range(n):
            x,y=numerator[i],denominator[i]
            gcd_val=m.gcd(x,y) #to reduce into simple fractions
            x//=gcd_val
            y//=gcd_val
            want_x,want_y=y-x,y # 1-(x/y) => (y-x)/y
            if (want_x,want_y) in fraction_map:
                counter+=fraction_map[(want_x,want_y)]
            fraction_map[(x,y)]+=1
        return counter
            
            


#{ 
 # Driver Code Starts

#Initial Template for Python 3

for _ in range(int(input())):
    n = int(input())
    numerator = list(map(int,input().split()))
    denominator = list(map(int,input().split()))
    ob = Solution()
    print(ob.countFractions(n,numerator,denominator))
    print("~")
# } Driver Code Ends