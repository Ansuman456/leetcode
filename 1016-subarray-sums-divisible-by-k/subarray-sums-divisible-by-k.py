class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        freq = {0: 1}
        prefix_sum = 0
        count = 0

        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k
            count += freq.get(remainder, 0)
            freq[remainder] = freq.get(remainder, 0) + 1

        return count