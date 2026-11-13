class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def isPossible(mid):
            count = 1
            currentSum = 0
            for num in nums:
                if currentSum + num <= mid:
                    currentSum += num
                else:
                    count += 1
                    currentSum = num
            return count <= k

        low = max(nums)
        high = sum(nums)
        ans = high

        while low <= high:
            mid = low + (high - low) // 2
            if isPossible(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
