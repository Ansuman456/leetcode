class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        k=k+1
        left=0
        window=set()
        check=False
        for right in range(len(nums)): #expand
            if(nums[right] in window):
                return True
            window.add(nums[right]) #expand calc

            if(right-left+1==k):
                window.remove(nums[left])
                left+=1
        
        return False
