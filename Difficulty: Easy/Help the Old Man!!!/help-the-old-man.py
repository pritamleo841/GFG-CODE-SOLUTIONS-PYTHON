#User function Template for python3

class Solution:
    def shiftPile(self, N, n):
        #Tower of Hanoi problem
        moves = []
        def towerOfHanoi(num,src,aux,dst):
            if num==0:
                return
            towerOfHanoi(num-1,src,dst,aux) #first dst used as auxilliary space
            moves.append((str(src),str(dst)))
            towerOfHanoi(num-1,aux,src,dst) #last src used as auxilliary space
        towerOfHanoi(N,1,2,3)
        return list(moves[n-1])


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, n = [int(x) for x in input().split()]
        
        ob = Solution()
        ans = ob.shiftPile(N, n)
        print(ans[0]+" "+ans[1])
        print("~")
# } Driver Code Ends