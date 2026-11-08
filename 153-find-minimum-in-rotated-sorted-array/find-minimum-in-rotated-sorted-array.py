class Solution:
    def findMin(self, nums: list[int]) -> int:
        low = 0
        high = len(nums) - 1
        ans = float('inf')

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] <= nums[high]:
                ans = min(ans, nums[mid])
                high = mid - 1

            else:
                low = mid + 1

        return ans