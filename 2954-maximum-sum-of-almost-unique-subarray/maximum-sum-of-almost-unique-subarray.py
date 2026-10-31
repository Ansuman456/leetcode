class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        left=0
        add=0
        ans=0
        window=dict() #freq wise store digits
        for right in range(len(nums)): #expand
            add+=nums[right] # expand calc
            window[nums[right]] = window.get(nums[right], 0) + 1


            if(right-left+1==k):
                if(len(window)>=m): #no of k:v pairs = no of unique elements in the dict
                    ans=max(ans,add) #process and store
                
                #shrink calc
                add-=nums[left]
                window[nums[left]] -= 1
                #remove no from window of no longer available
                if (window[nums[left]] == 0):
                    del window[nums[left]]

                left+=1
        
        return ans

