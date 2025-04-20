from collections import Counter
import heapq
class Solution :
    def rearrangeString(self, s):
        '''
        Use max heap and greedy approach-
        1. Count the frequency of each character.
        2. Use a max heap to always select the character with the highest remaining frequency (negate counts to simulate max heap in Python).
        3. At each step, pick the top character from the heap and ensure it's not the same as the previously placed character.
        4. If the previous character still has remaining frequency, push it back into the heap.
        
        If at any point there are no characters to choose (heap is empty) and the previous character still has count left, then it’s impossible → return "".
        '''
        freq=Counter(s)
        maxpq=[(-value,key) for key,value in freq.items()]
        heapq.heapify(maxpq)
        
        prev_char=None
        prev_freq=0
        res=[]
        
        while maxpq or prev_freq<0:
            if not maxpq and prev_freq<0:
                return ""
            freq,ch = heapq.heappop(maxpq)
            res.append(ch)
            #Push the previous char back if it still has frequency left
            if prev_freq<0:
                heapq.heappush(maxpq,(prev_freq,prev_char))
            #Update prev_char and prev_freq for next turn
            prev_freq=freq+1
            prev_char=ch
            
        return "".join(res)
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        str1 = input()
        solObj = Solution()
        str2 = solObj.rearrangeString(str1)
        if str2 == '':
            print(0)
        elif sorted(str1) != sorted(str2):
            print(0)
        else:
            for i in range(len(str2) - 1):
                if str2[i] == str2[i + 1]:
                    print(0)
                    break
            else:
                print(1)

        print("~")

# } Driver Code Ends