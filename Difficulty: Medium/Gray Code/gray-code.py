#User function Template for python3

class Solution:
    def graycode(self,n):
        '''
        1.A Gray code of N bits can be generated from the Gray code of N-1 bits:
        2.Take the Gray code for N-1 bits.
        3.Prefix 0 to all of them (in order).
        4.Prefix 1 to all of them (in reverse order).
        5.Combine both parts.
        '''
        if n==0:
            return ['']
        prev = self.graycode(n-1)
        return ['0'+code for code in prev]+['1'+code for code in reversed(prev)]


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import math
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        ob=Solution()
        l=ob.graycode(n)
        
        for x in l:
            print(x, end=" ")
            
        print()
     
        T-=1

        print("~")
if __name__=="__main__":
    main()
# } Driver Code Ends