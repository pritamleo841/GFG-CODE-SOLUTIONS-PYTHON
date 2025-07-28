class Solution:
    '''
    1.Initialize a heights[] array of size m (number of columns), initialized with zeros.
    2.For each row in the matrix:
        2a.Update heights[col]:
            If mat[row][col] == 1, add 1 to heights[col]
            Else, reset heights[col] = 0
        2b.Apply Largest Rectangle in Histogram algorithm on updated heights[]
        2c.Track the max area.
    '''
    def largest_rectangle_in_histogram(self,heights):
        stack = []
        max_area = 0
        heights.append(0)  # Sentinel to flush the stack at the end
    
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                # Width is i if stack is empty, else distance to previous lower
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
    
        heights.pop()  # Remove the sentinel
        return max_area
        
    def maxArea(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        n,m=len(matrix),len(matrix[0])
        heights=[0]*m
        max_area=0
        for row in matrix:
            #Update the histogram heights
            for i in range(m):
                heights[i]=heights[i]+1 if row[i]==1 else 0
            #Calculate max area for this histogram row
            max_area = max(max_area,self.largest_rectangle_in_histogram(heights))
        return max_area
        
        