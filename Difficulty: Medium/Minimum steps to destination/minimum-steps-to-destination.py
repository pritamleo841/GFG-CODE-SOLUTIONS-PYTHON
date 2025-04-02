#User function Template for python3

class Solution:
    def minSteps(self, d):
        '''
        diff=Sn−d
        If diff is even, we can flip a step from + to - to reduce the sum exactly by diff/2.
        If diff is odd, we need to take extra steps until diff becomes even.
        This works because flipping a step of value k (from +k to -k) reduces the total sum by 2k. 
        We need an even difference to be able to do this.
        '''
        if d==0:
            return 0
        steps=0
        sum_d=0
        while sum_d<d or (d-sum_d)%2!=0:
            steps+=1
            sum_d+=steps
        return steps


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        d = int(input())

        ob = Solution()
        print(ob.minSteps(d))

        print("~")
# } Driver Code Ends