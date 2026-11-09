class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        if(len(nums)==1):
            return 0
        low=0
        high=len(nums)-1
        while(low<=high):
            mid=low+(high-low)//2
            if(mid>0 and mid<len(nums)-1):
                if(nums[mid-1]<nums[mid]>nums[mid+1]):
                    return mid
            elif(mid==0):  # then peak is either mid or mid+1
                if(nums[mid]>nums[mid+1]):
                    return mid
                else:
                    return mid+1
            elif(mid==len(nums)-1):  # then peak is either mid or mid-1
                if(nums[mid-1]<nums[mid]):
                    return mid
                else:
                    return mid-1
            
            # compare mid with mid-1 and mid+1 and search in the side which is greater
            if(nums[mid-1]>nums[mid]): # search in left
                high=mid-1
            else:  #search in right
                low=mid+1        