from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        left = 0
        large = deque()
        result = []

        for right in range(len(nums)):

            while large and nums[large[-1]] < nums[right]:
                large.pop()

            large.append(right)

            if right - left + 1 == k:

                result.append(nums[large[0]])

                if large[0] == left:
                    large.popleft()

                left += 1

        return result