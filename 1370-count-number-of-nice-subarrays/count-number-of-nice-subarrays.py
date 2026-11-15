class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        for i in range(len(nums)):
            if(nums[i]%2==0):
                nums[i]=0
            else:
                nums[i]=1
         # if sum of sub array =k then no of 1's =k then no of odd's =k

        prefixSum = 0
        count = 0
        freq = {0: 1}
       
        for ele in nums:
            prefixSum += ele
            remaining = prefixSum - k

            if remaining in freq:  #subarray with sum k found
                count += freq[remaining]

            freq[prefixSum] = freq.get(prefixSum, 0) + 1
            
        return count