class Solution:
    def longestSubarray(self, nums, limit):

        large = []
        small = []

        left = 0
        maxlen = 0

        for right in range(len(nums)):

            # Maximum candidates
            while large and large[-1] < nums[right]:
                large.pop()

            large.append(nums[right])

            # Minimum candidates
            while small and small[-1] > nums[right]:
                small.pop()

            small.append(nums[right])

            # Shrink
            while large[0] - small[0] > limit:

                if nums[left] == large[0]:
                    large.pop(0)

                if nums[left] == small[0]:
                    small.pop(0)

                left += 1

            maxlen = max(maxlen, right - left + 1)

        return maxlen