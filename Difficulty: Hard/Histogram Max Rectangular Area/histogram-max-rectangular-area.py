
class Solution:
    def getMaxArea(self,arr):
        '''
        1.Traverse each bar in the histogram.
        2.Use a stack to keep track of indices of increasing bars.
        3.If current bar is lower than top of stack, calculate area:
        4.Height = height at top of stack (just popped)
        5.Width = distance between current index and index before the top of stack (after pop)
        6.Append a 0 at the end of the array to flush remaining bars.
        
        For each bar, you want to find:
            How far left you can extend (until a bar shorter than current)
            How far right you can extend
        You can only extend while heights are ≥ current height
        Stack helps track bars in increasing order so we can quickly find the previous taller/shorter bar
        '''
        stack=[] #store indices only
        max_area=0
        arr.append(0) #sentinal value
        for i,h in enumerate(arr):
            while stack and arr[stack[-1]]>h:
                height=arr[stack.pop()]
                width=i if not stack else i-stack[-1]-1
                area=height*width
                max_area=max(area,max_area)
            stack.append(i)
        return max_area