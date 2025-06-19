#User function Template for python3



#Function to generate binary numbers from 1 to N using a queue.
from collections import deque
def generate(N):
    #Use a queue to generate the next binary number by 
    #appending "0" and "1" to the current binary string.
    queue=deque()
    result=[]
    queue.append("1")
    
    for _ in range(N):
        current=queue.popleft()
        result.append(current)
        queue.append(current+"0")
        queue.append(current+"1")
    return result