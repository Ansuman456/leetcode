class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        left=0
        ans=0
        add=0
        window=set() # set stores unique ele in a window
        for right in range(len(nums)):
            #if nums[right] already present in window then shrink the window till previous occurance of nums[right] is removed from window
            while(nums[right] in window):
                #shrink until duplicate
                add-=nums[left]
                window.remove(nums[left])
                left+=1
            
            #expand(after no duplicate in window)
            add+=nums[right]
            window.add(nums[right])

            #shrinking
            if(right-left+1==k):
                #store result
                ans=max(ans,add)
                #shrink
                add-=nums[left]
                window.remove(nums[left])
                left+=1

        return ans

                