class Solution:
    def maxSumRangeQuery(self, nums, requests):
        n = len(nums)
        MOD = 10**9 + 7

        # Step 1: Calculate index frequencies
        diff = [0] * (n + 1)

        for start, end in requests:
            diff[start] += 1
            diff[end + 1] -= 1

        # Step 2: Reconstruct frequencies
        freq = [0] * n
        running = 0

        for i in range(n):
            running += diff[i]
            freq[i] = running

        # Step 3: Sort numbers and frequencies
        nums.sort()
        freq.sort()

        # Step 4: Calculate maximum sum
        ans = 0

        for num, count in zip(nums, freq):
            ans = (ans + num * count) % MOD

        return ans
