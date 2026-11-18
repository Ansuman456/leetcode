class Solution:
    def minZeroArray(self, nums, queries):
        n = len(nums)
        m = len(queries)

        def isPossible(k):
            diff = [0] * (n + 1)

            # Apply first k queries on difference array
            for i in range(k):
                l, r, val = queries[i]
                diff[l] += val
                diff[r + 1] -= val

            # Calculate prefix sum
            decrement = 0
            for i in range(n):
                decrement += diff[i]

                # Available decrement is insufficient
                if nums[i] > decrement:  #then nums[i] will be >0 after decrement 
                    return False

            return True

        # Already a zero array
        if all(x == 0 for x in nums):
            return 0

        # Binary search for minimum valid k
        low, high = 1, m
        ans = -1
        while low <= high:
            mid = low + (high - low) // 2
            if isPossible(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
