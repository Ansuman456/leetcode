class Solution:
    def isZeroArray(self, nums, queries):
        n = len(nums)
        diff = [0] * (n + 1)

        # Apply all queries on difference array
        for l, r in queries:
            diff[l] += 1
            diff[r + 1] -= 1

        # Calculate prefix sum and check
        decrement = 0

        for i in range(n):
            decrement += diff[i]
            # Available decrement is insufficient
            if nums[i] > decrement:
                return False

        return True
