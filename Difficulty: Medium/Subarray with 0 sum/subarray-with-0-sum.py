#User function Template for python3
class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr):
        seen_sum=set()
        summ=0
        for elem in arr:
            summ+=elem
            if summ==0:
                return True
            if summ in seen_sum:
                return True
            seen_sum.add(summ)
        return False
        #Return true or false


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]
        if (Solution().subArrayExists(arr)):
            print("true")
        else:
            print("false")

        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends