class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        large = []
        small = []
        limit=2
        left = 0
        ans = 0

        for right in range(len(nums)):
            # expand calc with large and small
            while large and large[-1] < nums[right]: #for large
                large.pop()
            large.append(nums[right])

            while small and small[-1] > nums[right]: #for small
                small.pop()
            small.append(nums[right])

            # Shrink
            while large[0] - small[0] > limit:
                # shrink calc in large and small
                if nums[left] == large[0]: #for large
                    large.pop(0)

                if nums[left] == small[0]: #for small
                    small.pop(0)
                
                left += 1

            if(large[0] - small[0] <= limit): #process and store
                ans+=right-left+1

        return ans       