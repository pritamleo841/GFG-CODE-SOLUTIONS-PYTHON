#User function Template for python3

class Solution:
    def totalFine(self, date, car, fine):
        #Code here
        summ=0
        if date%2==0:  # even date → fine odd cars
            for i in range(len(car)):
                if car[i]%2!=0:
                    summ+=fine[i]
        else:  # odd date → fine even cars
            for i in range(len(car)):
                if car[i]%2==0:
                    summ+=fine[i]
        return summ
        
    
    