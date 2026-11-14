class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        leftSum=0
        rightSum=0
        total=sum(nums)

        for i in range(0,len(nums)):
            if(i==0):
                leftSum=0
                rightSum=total-leftSum-nums[i]
            else:
                leftSum+=nums[i-1]
                rightSum=total-leftSum-nums[i]
            if(leftSum==rightSum):
                return i
        return -1