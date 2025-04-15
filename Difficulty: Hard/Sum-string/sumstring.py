#User function Template for python3
class Solution:
    def isSumString (ob,s):
        '''
         A string S is called sum-string if it satisfies the following properties:
            sub-string(i, x) + sub-string(x+1, j) = sub-string(j+1, l)
            and 
            sub-string(x+1, j)+sub-string(j+1, l) = sub-string(l+1, m) 
            and so on till end. 
        '''
        def string_sum(str1, str2):
            if len(str1) < len(str2):
                str1, str2 = str2, str1
            m, n = len(str1), len(str2)
            carry = 0
            ans = ""
            # Add common length parts from the end
            for i in range(1, n + 1):
                total = int(str1[-i]) + int(str2[-i]) + carry
                carry = total // 10
                ans = str(total % 10) + ans
            # Add remaining digits of longer number
            for i in range(n + 1, m + 1):
                total = int(str1[-i]) + carry
                carry = total // 10
                ans = str(total % 10) + ans
            if carry:
                ans = str(carry) + ans
            return ans
        
        
        def checkSumStrUtil(s, beg, len1, len2):
            s1 = s[beg:beg + len1]
            s2 = s[beg + len1:beg + len1 + len2]
            sum_str = string_sum(s1, s2)
            len3 = len(sum_str)
            next_start = beg + len1 + len2
            next_end = next_start + len3
            if next_end > len(s):
                return False
            if s[next_start:next_end] != sum_str:
                return False
            if next_end == len(s):
                return True
            return checkSumStrUtil(s, beg + len1, len2, len3)
        
        
        def isSumStr(s):
            n = len(s)
            for len1 in range(1, n):
                for len2 in range(1, n - len1):
                    if checkSumStrUtil(s, 0, len1, len2):
                        return 1
            return 0
            
        return isSumStr(s);

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=str(input())

        ob = Solution()
        
        print(ob.isSumString(S))
        print("~")
# } Driver Code Ends