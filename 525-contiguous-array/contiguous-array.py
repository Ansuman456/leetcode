
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Convert 0 to -1
        arr = [-1 if x == 0 else 1 for x in nums]
        n = len(arr)

        # Build prefix sum
        p = [0] * (n + 1)
        for i in range(n):
            p[i + 1] = p[i] + arr[i]

        # Find longest subarray with sum 0
        first_index = {}
        max_len = 0
        for i in range(n + 1):
            if p[i] in first_index:
                length = i - first_index[p[i]]
                max_len = max(max_len, length)
            else:
                first_index[p[i]] = i
                
        return max_len
