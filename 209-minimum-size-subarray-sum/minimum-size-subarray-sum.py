class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low=0
        high=0
        n=len(nums)
        add=0
        minSize=1000000 #10^6
        while(high<n):
            add+=nums[high] #expand
            # if sum>=target (condition satisfied)
            while(add>=target): #do shrinking until codition break again
                length=high-low+1
                minSize=min(minSize,length) # store before shrinking

                add-=nums[low] # shrink
                low+=1
            high+=1
        if(high==n and low==0):
            return 0
        return minSize