#User function Template for python3

class Solution:
    def steppingNumbers(self, n, m):
        count = 0  # Counter for stepping numbers
        def bfs(num):
            q = [num]
            local_count = 0
            while q:
                stepNum = q.pop(0)
                # Count the number if in range
                if n <= stepNum <= m:
                    local_count += 1  
                # If the number exceeds m, stop processing
                if stepNum == 0 or stepNum > m:
                    continue
                lastDigit = stepNum % 10
                # Generate next stepping numbers
                stepNumA = stepNum * 10 + (lastDigit - 1)
                stepNumB = stepNum * 10 + (lastDigit + 1)
                if lastDigit > 0 and stepNumA <= m:
                    q.append(stepNumA)
                if lastDigit < 9 and stepNumB <= m:
                    q.append(stepNumB)
            return local_count

        # Start BFS from each digit 0-9
        for i in range(10):
            count += bfs(i)
        return count
        
        '''
        TC:- O(n^2) solution
        def has_adjacent_diff_one(n):
            prevDigit = -1
            while(n):
                curDigit=n%10
                if (prevDigit == -1):
                    prevDigit = curDigit
                else:
                    if(abs(prevDigit-curDigit)!=1):
                        return False
                prevDigit=curDigit
                n//= 10
            return True
            
        count=0
        for i in range(n,m+1):
            if has_adjacent_diff_one(i):
                count+=1
        return count
        '''




#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        ob = Solution()
        N, M = map(int, input().split())
        ans = ob.steppingNumbers(N, M);
        print(ans)




        print("~")
# } Driver Code Ends