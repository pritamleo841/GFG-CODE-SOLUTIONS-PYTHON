class Solution:
    def sort012(self, arr):
        count={0:0,1:0,2:0}
        for elem in arr:
            if elem==0:
                count[0]+=1
            if elem==1:
                count[1]+=1
            if elem==2:
                count[2]+=1
        i=0
        while count[0]!=0:
            arr[i]=0
            i+=1
            count[0]-=1
        while count[1]!=0:
            arr[i]=1
            i+=1
            count[1]-=1
        while count[2]!=0:
            arr[i]=2
            i+=1
            count[2]-=1
        return arr
        
        