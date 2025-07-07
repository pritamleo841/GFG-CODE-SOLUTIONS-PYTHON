class Solution:
    def getSmaller(self, arr):
        '''
        Find Nearest Smaller to the Left for every index using a monotonic stack.
        Find Nearest Smaller to the Right for every index using the same technique but from the right.
        Combine results based on:
            Which is closer (distance).
                If equal distance: pick smaller height.
                If height is equal: pick smaller index.
        '''
        n=len(arr)
        left=[-1]*n
        right=[-1]*n
        stack=[]
        #Find nearest smaller to the left
        for i in range(n):
            while stack and arr[stack[-1]]>=arr[i]:
                stack.pop()
            if stack:
                left[i]=stack[-1]
            stack.append(i)
        stack.clear()
        #Find nearest smaller to the right
        for i in reversed(range(n)):
            while stack and arr[stack[-1]]>=arr[i]:
                stack.pop()
            if stack:
                right[i]=stack[-1]
            stack.append(i)
        result=[]
        for i in range(n):
            l=left[i]
            r=right[i]
            if l==-1 and r==-1:
                result.append(-1)
            elif r==-1:
                result.append(l)
            elif l==-1:
                result.append(r)
            else:
                dist_l=abs(i-l)
                dist_r=abs(i-r)
                if dist_l<dist_r:
                    result.append(l)
                elif dist_r<dist_l:
                    result.append(r)
                else:
                    # Same distance,prefer smaller height
                    if arr[l]<arr[r]:
                        result.append(l)
                    elif arr[r]<arr[l]:
                        result.append(r)
                    else:
                        result.append(min(l, r))  # Same height, choose smaller index
        return result
            
            
            
            
            
        