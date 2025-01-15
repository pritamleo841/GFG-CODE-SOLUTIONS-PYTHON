#User function Template for python3

class Solution:
    def lowerBound(self,temp,key):  #TC : O(logn)
        low,high=0,len(temp)-1
        answer=-1
        while low<=high:
            mid=low+(high-low)//2
            if temp[mid]>=key:
                answer=mid
                high=mid-1
            else:
                low=mid+1
        return answer
    #Function to find length of longest increasing subsequence.
    def lis(self, arr):
        # code here
        n=len(arr)
        temp=[arr[0]]
        length=1
        for i in range(1,n): #TC: O(n*logn)
            #If arr[i] is greater than temp's last element,
            #insert at temp's end
            if arr[i]>temp[-1]:
                temp.append(arr[i])
                length+=1 #increase length with each insertion at end
            else:
            #Find lower_bound of where arr[i] can be inserted
            #if found, replace the element of temp with arr[i]
                index = self.lowerBound(temp,arr[i])
                temp[index]=arr[i]
        #we don't need temp, so clear it
        temp.clear()
        return length
                
       



#{ 
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    for _ in range(int(input())):
        a = [int(x) for x in input().split()]
        ob = Solution()
        print(ob.lis(a))
        print("~")
# } Driver Code Ends