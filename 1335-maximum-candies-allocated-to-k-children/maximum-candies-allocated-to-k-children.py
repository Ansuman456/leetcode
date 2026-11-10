class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:
        if(sum(candies)<k):
            return 0
        
        def check(noOfCandies,arr):
            i=0
            noOfChildren=0
            for x in arr:
                noOfChildren += x // noOfCandies
            return noOfChildren

        low=1
        high=max(candies)
        ans=0
        while(low<=high):
            mid=low+(high-low)//2
            if(check(mid,candies.copy())>=k): # valid no of children -> increase noOfCandies
                ans=mid
                low=mid+1
            else:
                high=mid-1
        return ans