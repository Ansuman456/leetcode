# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()

        # STEP 1: Find Peak
        low = 0
        high = n - 1

        while low < high:
            mid = low + (high - low) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                low = mid + 1
            else:
                high = mid

        peak = low

        # STEP 2: Binary Search in Ascending Half
        low = 0
        high = peak

        while low <= high:
            mid = low + (high - low) // 2
            if mountainArr.get(mid) == target:
                return mid
            elif mountainArr.get(mid) < target:
                low = mid + 1
            else:
                high = mid - 1

        # STEP 3: Binary Search in Descending Half
        low = peak + 1
        high = n - 1

        while low <= high:
            mid = low + (high - low) // 2
            if mountainArr.get(mid) == target:
                return mid
            elif mountainArr.get(mid) < target:
                high = mid - 1
            else:
                low = mid + 1

        return -1