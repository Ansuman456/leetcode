
class Solution:
    def repairCars(self, ranks: list[int], cars: int) -> int:
        def canRepair(time):
            total = 0
            for r in ranks:
                total += int((time / r) ** 0.5)

                if total >= cars:
                    return True

            return False

        low = min(ranks)
        high = min(ranks) * cars * cars
        ans = high

        while low <= high:
            mid = low + (high - low) // 2

            if canRepair(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
