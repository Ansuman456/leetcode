class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_sum = 0
        # Store first occurrence of each remainder so that subarray be larger & lesser chances of len<2
        first_index = {0: -1}

        for i, num in enumerate(nums):
            prefix_sum += num
            # Handle k = 0 separately
            remainder = prefix_sum if k == 0 else prefix_sum % k

            if remainder in first_index:  
                # Subarray length must be at least 2
                if i - first_index[remainder] >= 2:
                    return True
            else:
                # Store only the first occurrence
                first_index[remainder] = i

        return False
