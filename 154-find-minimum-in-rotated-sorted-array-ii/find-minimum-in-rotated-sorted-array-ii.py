
class Solution:
    def findMin(self, nums: list[int]) -> int:
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = low + (high - low) // 2

            if nums[mid] < nums[high]:   # right side is sorted
                high = mid  #search in left

            elif nums[mid] > nums[high]:   # left side is sorted
                low = mid + 1  #search in right

            else:  # Ambiguous case: cannot identify sorted half
                high -= 1

        return nums[low]
