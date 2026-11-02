class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        odds=0
        left=0
        count=0
        ans=0
        for right in range(len(nums)):
            if(nums[right]%2!=0):
                odds+=1
                count=0 # no of valid substring while shrinking for nums[right]
            while(odds==k): #condition satisfied
                count+=1 # for fixed right, count each valid substring while shrinking 
                if(nums[left]%2!=0):
                    odds-=1
                left+=1
            ans+=count
        return ans
                
                

            