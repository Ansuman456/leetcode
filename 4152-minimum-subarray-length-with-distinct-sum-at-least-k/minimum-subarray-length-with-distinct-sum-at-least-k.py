class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        left = 0
        minlen = float('inf')
        add = 0
        window = {}

        for right in range(len(nums)):
            # Expand
            window[nums[right]] = window.get(nums[right], 0) + 1
            if window[nums[right]] == 1:
                add += nums[right]

            while add >= k:
                minlen = min(minlen, right - left + 1)

                #shrink
                window[nums[left]] -= 1
                if window[nums[left]] == 0:
                    add -= nums[left]
                left += 1

        return minlen if minlen != float('inf') else -1