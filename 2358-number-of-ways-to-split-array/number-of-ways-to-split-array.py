class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        leftSum=0
        rightSum=0
        total=sum(nums)
        count=0

        for i in range(0,len(nums)-1):
            if(i==0):
                leftSum=0
                rightSum=total-leftSum-nums[i]
            else:
                leftSum+=nums[i-1]
                rightSum=total-leftSum-nums[i]
            if(leftSum+nums[i]>=rightSum):
                count+=1
        return count      