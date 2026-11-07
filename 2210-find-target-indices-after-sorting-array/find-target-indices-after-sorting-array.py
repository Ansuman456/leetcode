class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:

        nums.sort()

        # Find first occurrence of target
        low = 0
        high = len(nums) - 1
        first = len(nums)

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] >= target: #store and search in left for first occ
                if nums[mid] == target:
                    first = mid
                high = mid - 1
            else:
                low = mid + 1

        # Find first element greater than target
        low = 0
        high = len(nums) - 1
        last = len(nums)

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] > target:    #store and search in left 
                last = mid
                high = mid - 1
            else:   #search in right
                low = mid + 1

        # Generate target indices
        return list(range(first, last))