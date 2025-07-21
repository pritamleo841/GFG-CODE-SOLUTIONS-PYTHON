
class Solution:
    def maxWater(self, height):
        '''
        At each position i, the amount of water trapped is:
            water[i]=min(max_left[i],max_right[i])−height[i]
            max_left[i]:The tallest bar to the left of index i (including i)
            max_right[i]:The tallest bar to the right of index i (including i)
        '''
        #TC-O(n), SC - o(1) => two pointer approach
        n=len(height)
        if n<=2:
            return 0
    
        left=0
        right=n-1
        left_max=0
        right_max=0
        trapped=0
    
        while left<right:
            if height[left]<height[right]:
                if height[left]>=left_max:
                    left_max=height[left]
                else:
                    trapped+=left_max-height[left]
                left+=1
            else:
                if height[right]>=right_max:
                    right_max=height[right]
                else:
                    trapped+=right_max-height[right]
                right-=1
    
        return trapped
        
        '''
        We use a monotonic decreasing stack to store the indices of the bars.
        As we traverse the array:
            When we find a bar taller than the top of the stack, it means we've found a right boundary.
            Pop the stack to get the bottom of the water container.
            The current index is the right wall, and the new top of the stack is the left wall.
            Compute the bounded height and width to find trapped water.
            
        #TC-O(n), SC - o(n) =>monotonic decreasing stack
        
        n=len(height)
        stack=[]
        water=0
    
        for i in range(n):
            # While current bar is taller than the top of the stack
            while stack and height[i]>height[stack[-1]]:
                top=stack.pop()
    
                if not stack:
                    break # No left boundary to trap water
    
                distance=i-stack[-1]-1  # Width between left and right walls
                bounded_height = min(height[i], height[stack[-1]])-height[top]
                water+=distance*bounded_height
    
            stack.append(i)
    
        return water
        '''
        