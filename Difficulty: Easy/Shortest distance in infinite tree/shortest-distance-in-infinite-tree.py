
class Solution:
    def distance(self,x, y):
        # code here
        #Try to match x and y values by dividing them by 2
        #maintain a count for each step
        #x=x>>1 equivalent to x=x//2 in python but faster
        count=0
        if x==y:
            return 0
        while x!=y:
            if x>y:
                x=x>>1
                count+=1
            else:
                y=y>>1
                count+=1
        return count


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        x = int(input())
        y = int(input())
        ob = Solution()
        print(ob.distance(x, y))
        print("~")

# } Driver Code Ends