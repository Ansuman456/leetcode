class Solution:
    def almostPalindromic(self, s: str) -> int:
        n = len(s)

        def expand(l, r):
            # First expand normally while characters match
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1

            # Mismatch found.
            # Option 1: delete s[l] and continue palindrome check
            l1, r1 = l - 1, r
            while l1 >= 0 and r1 < n and s[l1] == s[r1]:
                l1 -= 1
                r1 += 1

            # Option 2: delete s[r] and continue palindrome check
            l2, r2 = l, r + 1
            while l2 >= 0 and r2 < n and s[l2] == s[r2]:
                l2 -= 1
                r2 += 1

            return min(n, max(r1 - l1 - 1, r2 - l2 - 1))

        ans = 0

        for i in range(n):
            # Odd length
            ans = max(ans, expand(i, i))

            # Even length
            ans = max(ans, expand(i, i + 1))

        return ans