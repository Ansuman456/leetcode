class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        arr=nums+nums #now arr is circular array
        n=len(nums)
        left=0
        add=0
        minlen=float("inf")
        repeats=0
        remaining=target
        for ele in nums:
            add+=ele
        if target>add:  #repeatations of nums is required (infinite array)
            repeats = target // add
            remaining = target % add #new target after x repeatations

        if remaining == 0:
            return repeats * n
        
        add=0
        for right in range(len(arr)):
            add+=arr[right]
            while(add>remaining):
                add-=arr[left]
                left+=1
            if(add==remaining):   
                minlen=min(minlen,right-left+1)
        
        if minlen==0 or minlen==float("inf"):
            return -1
        else:
            return minlen+(repeats*n)
            




