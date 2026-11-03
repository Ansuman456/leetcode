class Solution:
    def countCompleteSubarrays(self, nums: list[int]) -> int:
        total = len(set(nums))

        def atmost(k):
            left = 0
            ans = 0
            d = {}

            for right in range(len(nums)):
                d[nums[right]] = d.get(nums[right], 0) + 1

                while len(d) > k:
                    d[nums[left]] -= 1

                    if d[nums[left]] == 0:
                        del d[nums[left]]

                    left += 1

                ans += right - left + 1

            return ans

        return atmost(total) - atmost(total - 1)