class Solution:
    def corpFlightBookings(self, bookings, n):
        diff = [0] * (n + 1)

        # Apply range updates
        for first, last, seats in bookings:
            l = first - 1
            r = last - 1

            diff[l] += seats
            diff[r + 1] -= seats

        # Reconstruct the final array
        ans = [0] * n
        running = 0

        for i in range(n):
            running += diff[i]
            ans[i] = running

        return ans
