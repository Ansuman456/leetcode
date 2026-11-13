import math
class Solution:
    def minimizedMaximum(self, n, quantities):
        def canDistribute(max_products):
            stores = 0
            for i in range(len(quantities)):
                stores += math.ceil(quantities[i] / max_products)
                if stores > n:
                    return False
            return True

        low = 1
        high = max(quantities)
        ans = high

        while low <= high:
            mid = (low + high) // 2
            if canDistribute(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans