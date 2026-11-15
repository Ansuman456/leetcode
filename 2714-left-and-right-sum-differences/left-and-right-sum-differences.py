class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum=0
        rightSum=0
        total=sum(nums)
        ans=[0]*len(nums)

        for i in range(0,len(nums)):
            if(i==0):
                leftSum=0
                rightSum=total-leftSum-nums[i]
            else:
                leftSum+=nums[i-1]
                rightSum=total-leftSum-nums[i]
            ans[i]=abs(rightSum-leftSum)
        return ans