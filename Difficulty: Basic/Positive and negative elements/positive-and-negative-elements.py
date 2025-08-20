#User function Template for python3



class Solution:
    def arranged(self,arr):
        n = len(arr)
        pos = []
        neg = []
        
        # separate positives & negatives
        for x in arr:
            if x >= 0:
                pos.append(x)
            else:
                neg.append(x)
        
        # interleave
        i = j = k = 0
        while i < len(pos) and j < len(neg):
            arr[k] = pos[i]   # place positive
            k += 1
            arr[k] = neg[j]   # place negative
            k += 1
            i += 1
            j += 1
        
        return arr
        