class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        def atmost(k):
            left=0
            ans=0
            add=0
            if k < 0:
                return 0
            for right in range(len(nums)):
                add+=nums[right]
                while(add>k):
                    add-=nums[left]
                    left+=1
                ans+=right-left+1
            return ans
        return atmost(goal)-atmost(goal-1)