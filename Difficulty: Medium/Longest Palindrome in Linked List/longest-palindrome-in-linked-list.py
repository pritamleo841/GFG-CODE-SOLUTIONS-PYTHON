# your task is to complete this function
# function should return an integer
'''
class node:
    def __init__(self):
        self.data = None
        self.next = Non
'''
'''
At each node:
1.Reverse the first part up to that node.
2.Compare the reversed part and the rest (forward direction).
3.Check both even and odd length palindromes.
'''
class Solution:
    def count_common(self,left, right):
        count = 0
        while left and right:
            if left.data == right.data:
                count += 1
                left = left.next
                right = right.next
            else:
                break
        return count
        
    def maxPalindrome(self,head):
        prev = None
        curr = head
        max_len = 0
        while curr:
            next_node = curr.next
            # Reverse current node's link
            curr.next=prev
            # Odd length palindrome (centered at curr)
            odd_len=2*self.count_common(prev, next_node) + 1
            # Even length palindrome (center between prev and curr)
            even_len=2*self.count_common(curr, next_node)
            max_len=max(max_len, odd_len, even_len)
            # Move forward in list
            prev = curr
            curr = next_node
    
        return max_len