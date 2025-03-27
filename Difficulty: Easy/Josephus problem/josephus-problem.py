#{ 
 # Driver Code Starts
import math



# } Driver Code Ends

#Complete this function

class Solution:
    def josephus(self,n,k):
        #J(n,k)=(J(n−1,k)+k)%n
        def recur(n,k):
            if n==1:
                return 0
            return (recur(n-1,k)+k)%n
        return recur(n,k)+1 #add 1 for 1-based indexing


#{ 
 # Driver Code Starts.
    
def main():
    
    T=int(input())
    
    while(T>0):
        n=int(input())
        k=int(input())
        print(Solution().josephus(n,k))
        
        T-=1

        print("~")
if __name__=="__main__":
    main()
# } Driver Code Ends