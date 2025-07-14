class Solution:
    def celebrity(self, mat):
        '''
        A celebrity is someone who:
            Is known by everyone (i.e., for all i ≠ c, mat[i][c] == 1)
            Knows no one else (i.e., for all j ≠ c, mat[c][j] == 0)

        We are given a square matrix mat[n][n] where:
            mat[i][j] == 1: person i knows person j
            mat[i][j] == 0: person i does not know person j
            mat[i][i] == 1: person knows themselves (irrelevant to the solution)
        '''
        n=len(mat)
        # Step 1: Find a candidate
        candidate = 0
        for i in range(1,n):
            if mat[candidate][i]==1:
                candidate=i
    
        # Step 2: Verify candidate
        for i in range(n):
            if i!=candidate:
                if mat[candidate][i]==1 or mat[i][candidate]==0:
                    return -1  # Not a celebrity
    
        return candidate