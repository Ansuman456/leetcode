class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left=0
        n=len(nums)
        ans=float('-inf') # result
        sum=0 # window
        for right in range(len(nums)):
            sum+=nums[right]

            if(right-left+1==k): #works after high>=k
                ans=max(ans,sum/k) # store avg before shrinking

                sum-=nums[left]
                left+=1
        
        return ans


