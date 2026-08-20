class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        left = 0
        count = 0
        k = 3
        window = {} #dictionary, not set
        # because if we are removing some charcter from window it is possible that another occurance of that char is still present in the window, so we decrement the count instead using dictionary

        for right in range(len(s)):
            # Expand
            window[s[right]] = window.get(s[right], 0) + 1 #on repeat increase count else 1

            # Window size = 3
            if right - left + 1 == k:
                if len(window) == k:
                    count += 1
                # Shrink
                window[s[left]] -= 1  # decrement char count in window 
                if window[s[left]] == 0: 
                    del window[s[left]] # the char is no longer present in window
                left += 1

        return count
