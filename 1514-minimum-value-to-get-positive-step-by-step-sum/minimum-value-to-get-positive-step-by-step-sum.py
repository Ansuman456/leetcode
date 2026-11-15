class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        add=0
        low=1
        for ele in nums:
            add+=ele
            low=min(low,add)
        #now low is the shortest in the prefix array
        if(low<1):
            startVal=1-low
            return startVal
        else:
            return 1
