class Solution:
    def maximumTastiness(self, price, k):
        def canSelect(price, k, diff):
            count = 1
            last_price = price[0]

            for i in range(1, len(price)):
                if price[i] - last_price >= diff:
                    count += 1
                    last_price = price[i]

                if count >= k:
                    return True
            return False

        price.sort()
        low = 0
        high = price[-1] - price[0]
        ans = 0

        while low <= high:
            mid = (low + high) // 2
            if canSelect(price, k, mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
