class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        firstocc=len(nums)
        lastocc=-1

        low=0
        high=len(nums)-1
        while(low<=high):
            mid=low+(high - low)//2
            if(nums[mid]==target): #search in left for first occurance
                firstocc=min(firstocc,mid)
                high = mid - 1
            elif(nums[mid] > target):   #search in left
                high = mid - 1
            else:    #search in right
                low = mid + 1
        
        low=0
        high=len(nums)-1
        while(low<=high):
            mid=low+(high - low)//2
            if(nums[mid]==target):  #search in right for last occurance
                lastocc = max(lastocc, mid)
                low = mid + 1
            elif(nums[mid] < target):     #search in right
                low = mid + 1
            else:   #search in left
                high = mid - 1
        
        if firstocc == len(nums):
            return [-1, -1]
        
        return [firstocc,lastocc]