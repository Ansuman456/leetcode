class Solution:
    def minEatingSpeed(self, piles, h):

        def check(k):
            hours = 0

            for pile in piles:
                hours += (pile + k - 1) // k

            return hours

        start = 1
        end = max(piles)

        while start <= end:
            mid = (start + end) // 2

            if check(mid) > h:
                start = mid + 1

            else:
                end = mid - 1

        return start