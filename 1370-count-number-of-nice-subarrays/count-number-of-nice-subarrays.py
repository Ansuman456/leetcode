class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:

        def atMost(k):
            left = 0
            odds = 0
            ans = 0

            for right in range(len(nums)):

                if nums[right] % 2 != 0:
                    odds += 1

                while odds > k:
                    if nums[left] % 2 != 0:
                        odds -= 1
                    left += 1

                ans += right - left + 1

            return ans

        return atMost(k) - atMost(k - 1)