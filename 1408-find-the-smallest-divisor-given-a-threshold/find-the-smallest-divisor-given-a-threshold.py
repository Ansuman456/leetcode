import math
class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        def check(divisor):
            add=0
            for ele in nums:
                add+=math.ceil(ele/divisor)
            return add
        
        low=1
        high=max(nums)
        ans=high
        while(low<=high):
            mid=low+(high-low)//2
            if(check(mid)<=threshold):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans