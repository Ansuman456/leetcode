class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda x: x[0])

        result = [points[0][:]]   # array at 0th index of points(2d)
        k = 0

        for i in range(1, len(points)):
            if result[k][1] >= points[i][0]:
                # Keep only the common intersection by shrinking
                # shooting multiple intervals by their intersection
                result[k][0] = max(result[k][0], points[i][0])
                result[k][1] = min(result[k][1], points[i][1])
            else:
                # shoot interval indivisual if no intersection
                result.append(points[i][:])  # array at ith index of points(2d)
                k += 1

        return len(result)