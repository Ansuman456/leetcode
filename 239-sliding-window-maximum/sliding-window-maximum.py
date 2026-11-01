class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        left=0
        large=[] #the ele are always in decreasing order
        result=[]
        for right in range(len(nums)):
            #expand
            while large and large[-1] < nums[right]:
                large.pop() #if(nums[right]>=nums[0]):
            # before inserting nums[right] we are removing the lesser ele from large
            large.append(nums[right])
            
            if(right-left+1==k):
                result.append(large[0]) # large[0] gives the max of the window
                #shrink
                if(nums[left]==large[0]): #if nums[left] in large then remove from there
                    large.pop(0)
                left+=1
        return result