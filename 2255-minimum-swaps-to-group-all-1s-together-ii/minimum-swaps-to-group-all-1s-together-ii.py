class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        #the window size will be the no of ones in nums
        k=0
        for ele in nums:
            if(ele==1):
                k+=1
        if(k==0):
            return 0
        #append k substring in end to handle cicular array
        nums.extend(nums[0:k])

        left=0
        ans=float('inf')
        zeros=0
        for right in range(len(nums)):
            if(nums[right]==0):
                zeros+=1

            if(right-left+1==k):
                #store before shrinking
                ans=min(ans,zeros)
                #shrink
                if(nums[left]==0):
                    zeros-=1
                left+=1
        
        return ans
