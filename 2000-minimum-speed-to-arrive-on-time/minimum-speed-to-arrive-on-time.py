
import math

class Solution:
    def minSpeedOnTime(self, dist: list[int], hour: float) -> int:
        def canArrive(speed):
            total = 0
            for i in range(len(dist)):
                time = dist[i] / speed

                if i == len(dist) - 1:
                    total += time
                else:
                    total += math.ceil(time)
            return total <= hour

        low = 1
        high = 10**7
        ans = -1
        while low <= high:
            mid = low + (high - low) // 2
            if canArrive(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
