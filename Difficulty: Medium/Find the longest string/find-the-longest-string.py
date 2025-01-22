#User function Template for python3


class Solution():
    def longestString(self, arr, n):
        #your code goes here
        #TC : O(nlogn), SC: O(N)
        #sort the strings lexographically
        arr.sort()
        #store each string in a dictionary
        myDict = {}
        for elem in arr:
            if elem in myDict:
                myDict[elem] += 1
            else:
                myDict[elem] = 1 
        
        ans=""
        size=float('-inf')
        #for each word in arr
        for elem in arr:
            temp=""
            count=0
            n=len(elem)
            # check if it's prefix are present
            for i in range(n):
                temp+=elem[i]
                #each prefix should be present in the map
                if myDict.get(temp)!=None:
                    count+=1
            # if all prefix are present and 
            #the current size is longest, update the ans
            if count==n and n>size:
                size=n
                ans=elem
        return ans
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [i for i in input().split()]
        print(Solution().longestString(arr,n))
        print("~")
# } Driver Code Ends