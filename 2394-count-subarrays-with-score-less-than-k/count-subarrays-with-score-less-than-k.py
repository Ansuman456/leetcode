class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        add=0
        score=0
        left=0
        ans=0
        for right in range(len(nums)):
            add+=nums[right]
            score=add*(right-left+1)
            while(score>=k):
                add-=nums[left]
                left+=1
                score=add*(right-left+1)
            ans+=right-left+1
        return ans

