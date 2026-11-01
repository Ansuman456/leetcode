class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        left=0
        maxsum=0
        add=0
        window=set()
        for right in range(len(nums)):
            while(nums[right] in window): #shrink
                window.remove(nums[left])
                add-=nums[left]
                left+=1
            
            #now window has no duplicates, expand
            window.add(nums[right])
            add+=nums[right]
            #process and store
            maxsum=max(maxsum,add)
        return maxsum

