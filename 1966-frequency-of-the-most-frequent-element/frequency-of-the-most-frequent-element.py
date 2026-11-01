class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        operations=0
        left=0
        windowsum=0
        maxlen=0
        nums.sort()
        
        for right in range(len(nums)):
            windowsum+=nums[right]
            while((nums[right]*(right-left+1))-windowsum >k):
                windowsum-=nums[left]
                left+=1
            maxlen=max(maxlen,right-left+1)
        return maxlen


        