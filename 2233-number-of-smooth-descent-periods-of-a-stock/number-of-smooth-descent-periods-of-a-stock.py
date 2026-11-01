class Solution:
    def getDescentPeriods(self, prices: list[int]) -> int:
        if(len(prices)==1):
            return 1
        result=0
        #for starting element
        count=1
        result+=count
        
        for right in range(1,len(prices)):
            if(prices[right]+1==prices[right-1]):
                count+=1
            else: #new period
                count=1 #reset
            result+=count
        return result
