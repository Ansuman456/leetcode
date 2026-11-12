class Solution:
    def maxDistance(self, position, m):
        def canPlace(position, m, dist):
            count = 1
            last_pos = position[0]

            for i in range(1, len(position)):
                if position[i] - last_pos >= dist:
                    count += 1
                    last_pos = position[i]

                if count >= m:
                    return True

            return False

        position.sort()
        low = 1
        high = position[-1] - position[0]
        ans = 0

        while low <= high:
            mid = (low + high) // 2

            if (canPlace(position, m, mid)):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans