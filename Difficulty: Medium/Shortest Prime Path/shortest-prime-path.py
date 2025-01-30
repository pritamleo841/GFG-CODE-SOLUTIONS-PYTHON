#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
'''
        1.Generate all four-digit prime numbers using the Sieve of Eratosthenes.
        2.Use BFS to find the shortest path from num1 to num2.
        3.Modify one digit at a time and check if the new number is prime.
        4.Keep track of visited numbers to avoid cycles.
'''
from collections import deque
class Solution:
    def getAllPrimes(self):
        """Generates all four-digit prime numbers using the Sieve of Eratosthenes."""
        primes = set()
        is_prime = [True] * 10000
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
        
        for num in range(2, 10000):
            if is_prime[num]:
                if num >= 1000:  # Only consider four-digit primes
                    primes.add(num)
                for multiple in range(num * num, 10000, num):  # Start from num^2
                    is_prime[multiple] = False
        return primes
    
    def getNextPrimes(self, current, primes):
        """Generates all valid numbers that differ by one digit and are prime."""
        neighbors = []
        str_num = list(str(current))
        
        for i in range(4):  # Four digits
            original_digit = str_num[i]
            for d in "0123456789":  # Try replacing with 0-9
                if d != original_digit:
                    str_num[i] = d
                    new_num = int("".join(str_num))
                    if new_num in primes:  # Must be prime and four-digit
                        neighbors.append(new_num)
            str_num[i] = original_digit  # Restore the original digit
        return neighbors
    
    def solve(self, num1, num2):
        if num1 == num2:
            return 0
        
        primes = self.getAllPrimes()  # Get all four-digit primes
        queue = deque([num1])  # BFS queue (number)
        visited = set([num1])
        steps = 0  # Track level count
        
        while queue:
            size = len(queue)  # Number of nodes at the current level
            for _ in range(size):  # Process all nodes in the current BFS level
                current = queue.popleft()
                
                for neighbor in self.getNextPrimes(current, primes):
                    if neighbor == num2:
                        return steps + 1
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            
            steps += 1  # Move to the next BFS level
        
        return -1  # If num2 is unreachable

        




#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        num1,num2=map(int,input().split())
        ob = Solution()
        print(ob.solve(num1,num2))
        print("~")
# } Driver Code Ends