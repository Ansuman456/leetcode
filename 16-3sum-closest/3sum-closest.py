class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        result=[]
        n=len(nums)
        nums.sort() 
        closest=nums[0] + nums[1] + nums[2]
        for k in range(0,n-2):
            i=k+1
            j=n-1
            while(i<j):
                temp=nums[i]+nums[j]+nums[k]
                if abs(target-temp)<abs(target-closest): #curent triplet is closer
                    closest=temp
                
                if nums[i]+nums[j]+nums[k]<target:
                    i+=1
                else:
                    j-=1
        
        return closest