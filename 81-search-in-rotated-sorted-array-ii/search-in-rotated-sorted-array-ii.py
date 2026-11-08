class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return True

            # Ambiguous case: cannot identify sorted half
            if nums[low] == nums[mid] == nums[high]:  # cause if nums[mid] is not an answer, then nums[low] and nums[high] also dont, so better discard them
                low += 1
                high -= 1

            # Left half is sorted
            elif nums[low] <= nums[mid]:

                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            # Right half is sorted
            else:

                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return False