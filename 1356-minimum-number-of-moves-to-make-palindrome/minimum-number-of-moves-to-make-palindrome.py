class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        s = list(s)
        count = 0

        i = 0
        j = len(s) - 1

        while i < j:
            # Already matching
            if s[i] == s[j]:
                i += 1
                j -= 1
                continue

            # Find matching character for s[i]
            k = j # correct place
            while k > i and s[k] != s[i]:
                k -= 1

            if k == i:  # No match found, s[i] is the middle character
                # move one step towards centre
                s[k], s[k + 1] = s[k + 1], s[k]
                count += 1
            else:
                # Move matching character to position j(correct place)
                while k < j:
                    s[k], s[k + 1] = s[k + 1], s[k]
                    k += 1
                    count += 1

                # Pair is fixed
                i += 1
                j -= 1

        return count
