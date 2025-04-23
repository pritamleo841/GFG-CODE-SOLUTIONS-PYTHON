#User function Template for python3

class Solution:
    def countWords(self,List, n):
        freq={}
        for word in List:
            freq[word]=freq.get(word,0)+1
        count=0
        for key,val in freq.items():
            if val==2:
                count+=1
        return count
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        n = int(input())
        List = input().split()
        ob = Solution()
        print(ob.countWords(List, n))
        print("~")
# } Driver Code Ends