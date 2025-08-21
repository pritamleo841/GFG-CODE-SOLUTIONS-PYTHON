from collections import Counter
class Solution:
    #Function to find all elements in array that appear more than n/k times.
    def countOccurence(self,arr, k):
        n = len(arr)
        freq = Counter(arr)   # counts frequency of each element
        result = []
        for key, count in freq.items():
            if count > n // k:
                result.append(key)
        return len(result)