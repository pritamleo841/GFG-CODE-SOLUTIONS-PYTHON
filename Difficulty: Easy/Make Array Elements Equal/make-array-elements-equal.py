#User function Template for python3

class Solution:
    def minOperations(self, N):
        '''
        We have - 
        arr[i] = 2i + 1 (0 ≤ i < N),
        the first N odd numbers. Any operation “+1 to one, −1 from another” preserves the total sum, so all elements must end up at the average:
        
        target = (∑arr) / N.
        
        Sum of first N odd numbers is N², so target = N.
        
        Only elements below N need increments; the total number of operations equals the total deficit of those elements.
        
        Case 1: N even, N = 2m
        
        Numbers < N are the first m odds: 1, 3, …, 2m−1.
        Deficit of each is (2m − (2i+1)) for i = 0,…,m−1.
        
        Total operations = ∑(2m − (2i+1)) from i=0 to m−1
        = m⋅2m − (1+3+…+(2m−1))
        = 2m² − m²
        = m²
        = (N²)/4.
        
        Case 2: N odd, N = 2m+1
        
        Numbers < N are 1, 3, …, 2m−1 (m of them).
        Deficit of each is (2m+1) − (2i+1) = 2(m−i).
        
        Total operations = ∑2(m−i) from i=0 to m−1
        = 2(1+2+…+m)
        = 2⋅(m(m+1)/2)
        = m(m+1).
        
        Express in terms of N:
        m(m+1) = ((2m+1)² − 1)/4 = (N² − 1)/4.
        
        Final formula:
        
        min_ops =
        (N² / 4), if N is even
        ((N² − 1) / 4), if N is odd
        
        Quick intuition:
        The array is symmetric around N. Pair each low element with a high element equidistant from N; each pair needs exactly the distance-to-N moves, and summing those distances over the lower half gives the formulas above.
        '''
        
        
        if N%2==0:
            return ((N*N)//4)
        else:
            return (((N*N)-1)//4)
        
        
        
        
        
        