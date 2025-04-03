# User function Template for python3

class Solution:
    def  towerOfHanoi(self, n, fromm, to, aux):
        return (1<<n)-1  #Equivalent to 2^n - 1
        '''
        moves=[0]
        def recur(n, fromm, to, aux):
            if n==1:
                moves[0]+=1
                return
            recur(n-1,fromm,aux,to)
            moves[0]+=1
            recur(n-1,aux,to,fromm)
        recur(n,fromm,to,aux)
        return moves[0]
        '''


#{ 
 # Driver Code Starts
# Initial Template for Python 3

import math


def main():

    T = int(input())

    while (T > 0):
        N = int(input())
        ob = Solution()
        print(ob.towerOfHanoi(N, 1, 3, 2))
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends