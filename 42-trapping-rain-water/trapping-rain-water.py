class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 2: # water can't be stored
            return 0

        # max height to the left of each index
        maxLeft = [0] * n
        maxLeft[0] = height[0]
        for i in range(1, n):
            maxLeft[i] = max(maxLeft[i - 1], height[i])

        # max height to the right of each index
        maxRight = [0] * n
        maxRight[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            maxRight[i] = max(maxRight[i + 1], height[i])

        # calculate trapped water
        water = 0
        for i in range(n):
            water += min(maxLeft[i], maxRight[i]) - height[i]

        return water