class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        prefixSum = [0] * (n + 1)
        for i in range(n): # build prefix array
            prefixSum[i + 1] = prefixSum[i] + nums[i]

        subarraySums = []  # sum of all subarray [n * (n + 1) / 2 elements]

        for i in range(n):   
            for j in range(i, n):
                subarraySums.append(prefixSum[j + 1] - prefixSum[i])

        subarraySums.sort()

        return sum(subarraySums[left - 1:right]) % (10**9 + 7)   
        #its left-1 and right, not left and right+1 cause give problem is 1 indexed