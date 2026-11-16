class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        prefix_sum = 0
        max_len = 0

        # Store first occurrence of prefix sums
        first_index = {0: -1}

        for i, h in enumerate(hours):
            # Transform the value
            if h > 8:
                prefix_sum += 1
            else:
                prefix_sum -= 1

            # Case 1: Entire prefix is valid
            if prefix_sum > 0:
                max_len = i + 1

            # Case 2: Find an earlier prefix sum
            elif prefix_sum - 1 in first_index:
                length = i - first_index[prefix_sum - 1]
                max_len = max(max_len, length)

            # Store only the first occurrence
            if prefix_sum not in first_index:
                first_index[prefix_sum] = i

        return max_len
