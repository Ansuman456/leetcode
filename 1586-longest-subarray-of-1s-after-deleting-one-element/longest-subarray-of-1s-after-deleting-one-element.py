class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        zeros=0
        left=0
        maxlen=0
        for right in range(len(nums)):
            if(nums[right]==0):
                zeros+=1
            while(zeros>1):
                if(nums[left]==0):
                    zeros-=1
                left+=1
            maxlen=max(maxlen,right-left+1)
        return maxlen-1