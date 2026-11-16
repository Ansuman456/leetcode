class Solution:
    def carPooling(self, trips, capacity):
        diff = [0] * 1001

        # Apply all trip updates
        for passengers, start, end in trips:
            diff[start] += passengers
            diff[end] -= passengers

        # Calculate running passenger count
        current = 0

        for change in diff:
            current += change
            if current > capacity:
                return False

        return True
