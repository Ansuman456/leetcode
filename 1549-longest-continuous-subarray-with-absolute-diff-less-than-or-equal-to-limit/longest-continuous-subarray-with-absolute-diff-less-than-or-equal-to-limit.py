class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        large=[]
        small=[]
        left=0
        maxlen=0
        for right in range(len(nums)):
            #expand -> update large and small
            while large and nums[large[-1]] < nums[right]:
                large.pop() # for large
            large.append(right)

            while small and nums[small[-1]] > nums[right]:
                small.pop() # for small
            small.append(right)

            while large and small and nums[large[0]] - nums[small[0]] > limit: #shrink
                #update in large and small
                if(left==large[0]): # for large
                    large.pop(0)
                if(left==small[0]): # for small
                    small.pop(0)
                left+=1

            if large and small and nums[large[0]] - nums[small[0]] <= limit:
                # large[0] and small[0] are the max and min of current window
                maxlen=max(maxlen,right-left+1)
        return maxlen
        