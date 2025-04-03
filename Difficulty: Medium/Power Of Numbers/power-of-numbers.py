#User function Template for python3

class Solution:
    def reverse_exponentiation(self, n):
        def reverse(n):
            return int(str(n)[::-1])
        def power(n,r):
            if r==0:
                return 1
            if r%2==1:
                return n*power(n,r-1)
            if r%2!=1:
                return power(n,r//2)**2
        r = reverse(n)
        return power(n,r)


#{ 
 # Driver Code Starts
# Input handling
if __name__ == "__main__":
    T = int(input())  # test cases

    for _ in range(T):
        n = int(input())  # input N
        solution = Solution()
        ans = solution.reverse_exponentiation(n)
        print(ans)

# } Driver Code Ends