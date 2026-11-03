class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        def atMost(k):
            left=0
            count=0
            d=dict()
            for right in range(len(nums)):
                d[nums[right]]=d.get(nums[right],0)+1
                while(len(d)>k):
                    d[nums[left]]=d.get(nums[left])-1
                    if(d[nums[left]]==0):
                        del d[nums[left]]
                    left+=1
                count+=right-left+1
            return count
        return atMost(k) - atMost(k - 1)
