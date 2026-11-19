class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        small = min(nums)
        large = max(nums)

        offset = k - small
        size = large + k + offset + 2

        diff = [0] * size
        freq = {}
        ans = 0

        # Build difference array and frequency dictionary
        for ele in nums:
            freq[ele] = freq.get(ele, 0) + 1

            start = ele - k + offset
            end = ele + k + offset

            diff[start] += 1
            diff[end + 1] -= 1

        # Build prefix sum (cumsum)
        cumsum = [0] * size
        cumsum[0] = diff[0]

        for i in range(1, size):
            cumsum[i] = cumsum[i - 1] + diff[i]

        # Calculate maximum possible frequency
        for target in range(small - k, large + k + 1):
            idx = target + offset

            add = cumsum[idx]
            alreadyfreq = freq.get(target, 0)

            operationsRequired = add - alreadyfreq

            maxpossiblefreq = min(
                operationsRequired,
                numOperations
            )

            ans = max(
                ans,
                alreadyfreq + maxpossiblefreq
            )

        return ans
