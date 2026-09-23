class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        check = True

        # Helper function using your variable style
        def isPalindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            elif s[i] != s[j]:
                # Check both possibilities: skip left or skip right
                check = isPalindrome(i + 1, j) or isPalindrome(i, j - 1)
                return check
            else:  # mismatch and no skip left
                return False

        return check
                
