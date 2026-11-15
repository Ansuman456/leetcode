class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = 0
        count = 0

        freq = {0: 1}

        for num in nums:
            prefixSum += num
            remaining = prefixSum - k

            if remaining in freq:  #subarray with sum k found
                count += freq[remaining]

            freq[prefixSum] = freq.get(prefixSum, 0) + 1

        return count