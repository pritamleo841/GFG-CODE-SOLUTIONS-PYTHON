#User function Template for python3
'''
Level input isn’t necessary (if we ignore max position limit) because first elements are same.
The result is based on count of 1’s in binary representation of position minus one. If count of 1’s is even then result is Engineer, else then Doctor.
And of course position limit is 2^(Level-1)
'''
class Solution:
    def profession(self, level, pos):
        #Function to get no of set bits in binary representation of passed binary no.
        def countSetBits(n):
            count = 0
            while n>0:
              n &= (n-1)
              count+=1
            return count
  
        # Returns 'e' if profession of node at given level
        # and position is engineer. Else doctor. The function
        # assumes that given position and level have valid values.
        c=countSetBits(pos-1)
        # If set bit count is odd, then doctor, else engineer
        if c%2==0:
            return 'e'
        else:
            return 'd'
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        level, pos = [int(x) for x in input().split()]
        
        ob = Solution()
        if(ob.profession(level, pos) == 'd'):
            print("Doctor")
        else:
            print("Engineer")
        print("~")
# } Driver Code Ends