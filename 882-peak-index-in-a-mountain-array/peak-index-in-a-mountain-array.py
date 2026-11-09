class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        low=0
        high=len(arr)-1
        while(low<=high):
            mid=low+(high-low)//2
            if(mid>0 and mid<len(arr)-1):
                if(arr[mid-1]<arr[mid]>arr[mid+1]):
                    return mid
            elif(mid==0):  # then peak is either mid or mid+1
                if(arr[mid]>arr[mid+1]):
                    return mid
                else:
                    return mid+1
            elif(mid==len(arr)-1):  # then peak is either mid or mid-1
                if(arr[mid-1]<arr[mid]):
                    return mid
                else:
                    return mid-1
            
            # compare mid with mid-1 and mid+1 and search in the side which is greater
            if(arr[mid-1]>arr[mid]): # search in left
                high=mid-1
            else:  #search in right
                low=mid+1

