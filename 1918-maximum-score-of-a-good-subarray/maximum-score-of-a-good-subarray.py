class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        # def minimum(nums, i, j):
        #     low = nums[i]
        #     for l in range(i, j + 1):
        #         if nums[l] < low:
        #             low = nums[l]
        #     return low

        i = k
        j = k
        minimum = nums[k]
        score = nums[k]
        while i > 0 or j < len(nums) - 1:
            if i == 0:  # if i reached edge move j only
                j += 1
            elif j == len(nums) - 1: # if j reached edge move i only
                i -= 1
            elif nums[i - 1] >= nums[j + 1]: #move tomwards bigger side to maximize score
                i -= 1
            else:
                j += 1
            # Since each step only adds one new element, you don't need to recalculate the minimum for each window
            #temp = (j - i + 1) * minimum(nums, i, j)
            minimum = min(minimum, nums[i], nums[j])
            temp=(j - i + 1)*minimum
            
            score = max(score, temp)

        # Single element [k]
        score = max(score, nums[k])
        return score