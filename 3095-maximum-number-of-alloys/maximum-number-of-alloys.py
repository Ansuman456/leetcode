class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int,
                         composition: list[list[int]],
                         stock: list[int],
                         cost: list[int]) -> int:

        def check(x):
            # Try every machine
            for i in range(k):
                totalCost = 0

                for j in range(n):
                    required = composition[i][j] * x
                    buy = max(0, required - stock[j])

                    totalCost += buy * cost[j]

                    # No need to calculate further
                    if totalCost > budget:
                        break

                if totalCost <= budget:
                    return True

            return False   

        low = 0
        high = 10**9
        ans = 0

        while low <= high:
            mid = low + (high - low) // 2

            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans