class Solution:
    def shiftingLetters(self, s, shifts):
        n = len(s)
        diff = [0] * (n + 1)

        # Step 1: Apply range updates
        for start, end, direction in shifts:
            val = 1 if direction == 1 else -1

            diff[start] += val
            diff[end + 1] -= val

        # Step 2: Calculate prefix sum
        running = 0
        result = []

        # Step 3: Apply total shift to each character
        for i in range(n):
            running += diff[i]

            shift = running % 26

            new_char = chr(
                (ord(s[i]) - ord('a')  #convert ord(s[i])Ascii to 0-25 by -ord('a') and
                + shift) % 26  # add the shift,  do %26 in case: {ord(s[i]) - ord('a') + shift} to goes >25
                + ord('a')    # again convert to ascii by + ord('a') 
            )

            result.append(new_char)

        return ''.join(result)
