#User function Template for python3
import math
def countminreversals(s):
    '''
    Only even-length strings can be balanced.
        If the length of s is odd,return -1 immediately.
    
    We need to count:
        The number of unmatched left braces ({)
        The number of unmatched right braces (})
    Using these counts, the minimum number of reversals needed is:
        math.ceil(left_brace / 2) + math.ceil(right_brace / 2)
    '''
    n=len(s)
    if n%2!=0:
        return -1
    right_brace=0
    left_brace=0
    for ch in s:
        if ch=='{':
            left_brace+=1
        else:   #ch=='}'
            if left_brace>0:
                left_brace-=1
            else:
                right_brace+=1
    return math.ceil(left_brace/2)+math.ceil(right_brace/2)
            
    
    