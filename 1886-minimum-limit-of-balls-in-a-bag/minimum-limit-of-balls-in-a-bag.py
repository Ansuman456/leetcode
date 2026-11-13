import math
class Solution:
    def minimumSize(self, nums, maxOperations):
        def canSplit(nums, maxOperations, max_balls):
            operations = 0
            for i in range(len(nums)):
                operations += math.ceil(nums[i] / max_balls) - 1
                if operations > maxOperations:
                    return False
            return True

        low = 1
        high = max(nums)
        ans = high

        while low <= high:
            mid = (low + high) // 2
            if canSplit(nums, maxOperations, mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
