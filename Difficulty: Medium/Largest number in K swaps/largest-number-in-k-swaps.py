#User function Template for python3

class Solution:
    #Function to find the largest number after k swaps.
    def findMaximumNum(self,s,k):
        max_val=[s]

        def swap(string,i,j):
            lst=list(string)
            lst[i],lst[j]=lst[j],lst[i]
            return ''.join(lst)

        def helper(string, k):
            if k==0:
                return

            n=len(string)
            for i in range(n-1):
                max_char=max(string[i+1:])  # only consider swaps with larger chars
                if max_char>string[i]:
                    for j in range(i+1,n):
                        if string[j]==max_char:
                            swapped_str=swap(string, i, j)
                            if swapped_str>max_val[0]:
                                max_val[0]=swapped_str
                            helper(swapped_str, k - 1)

        helper(s,k)
        return max_val[0]
        '''
        1010/1011 test cases passed ->
        
        max_val = [s]
        
        def swapped(string,i,j):
            if i==j:
                return string
            return string[:i]+string[j]+string[i+1:j]+string[i]+string[j+1:]
            
        def maximum(string,k):
            if string>max_val[0]:
                max_val[0]=string
            if k==0:
                return
            #check for each consecutive charcters
            for i in range(len(string)-1):
                for j in range(i+1,len(string)):
                    if string[j]>string[i]:
                        swapped_string=swapped(string,i,j)
                        maximum(swapped_string,k-1)
                        #no need for backtracking since not changing the original string
        maximum(s,k)               
        return max_val[0]
        '''
        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        k = int(input())
        s = input()
        ob=Solution()
        print(ob.findMaximumNum(s,k))

        print("~")
# } Driver Code Ends