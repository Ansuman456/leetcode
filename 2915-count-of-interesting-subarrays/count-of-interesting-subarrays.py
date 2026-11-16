class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        # Transform the original array into 0s and 1s
        arr = [1 if num % modulo == k else 0 for num in nums]

        prefix_sum = 0
        count = 0
        # Store frequency of prefix remainders
        prefix_freq = {0: 1}

        for num in arr:
            prefix_sum += num
            # Current prefix remainder
            remainder = prefix_sum % modulo
            # Required previous remainder.
            required = (remainder - k) % modulo
            # Count valid subarrays ending at current index
            count += prefix_freq.get(required, 0)
            # Store current prefix remainder
            prefix_freq[remainder] = prefix_freq.get(remainder, 0) + 1

        return count
