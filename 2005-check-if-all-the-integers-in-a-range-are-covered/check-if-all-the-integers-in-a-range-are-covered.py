class Solution:
    def isCovered(self, ranges, left, right):
        diff = [0] * 52

        # Mark range coverage
        for start, end in ranges:
            diff[start] += 1
            diff[end + 1] -= 1

        # Calculate prefix sum
        coverage = 0

        for i in range(1, 52):
            coverage += diff[i]

            # Check only the required range
            if left <= i <= right:
                if coverage == 0:
                    return False

        return True
