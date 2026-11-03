class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        largest = max(nums)
        count=0
        left=0
        ans=0
        n=len(nums)
        for right in range(len(nums)):
            if(nums[right]==largest):
                count+=1
            while(count>=k):
                ans+=n-right
                if(nums[left]==largest):
                    count-=1
                left+=1
        return ans
            