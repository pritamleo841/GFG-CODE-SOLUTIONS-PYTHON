#User function Template for python3
import heapq
class Solution:
    def sortedMatrix(self,N,Mat):
        #=O(N^2 \log N) time.
        # Flatten the matrix into a list
        flat_list = [Mat[i][j] for i in range(N) for j in range(N)]
        
        # Convert the list into a min-heap (O(N^2))
        heapq.heapify(flat_list)
        
        # Extract min elements and put them back into the matrix (O(N^2 log N^2))
        for i in range(N):
            for j in range(N):
                Mat[i][j] = heapq.heappop(flat_list)
        
        return Mat
        '''
        temp=[]
        for i in range(n):
           for j in range(n):
                temp.append(mat[i][j])
        temp.sort()
        k=0
        for i in range(n):
            for j in range(n):
                mat[i][j]=temp[k]
                k+=1
        return mat
        '''