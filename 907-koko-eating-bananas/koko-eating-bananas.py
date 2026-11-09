class Solution:
    def minEatingSpeed(self, piles, h):

        def check(k):
            hours = 0

            for pile in piles:
                hours += (pile + k - 1) // k

            return hours

        low = 1
        high = max(piles)
        ans = -1

        while low <= high:
            mid = low + (high - low) // 2

            if check(mid) <= h:  # Valid speed, search left
                ans = mid
                high = mid - 1 #decrease speed

            else:  # Invalid speed, search right
                low = mid + 1   #increase speed

        return ans