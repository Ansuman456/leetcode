class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        n=len(nums)
        ans=[]
        for l in range(0,n-3):
            if(l>0 and nums[l]==nums[l-1]):
                continue
            for k in range(l+1,n-2):
                if(k>l+1 and nums[k]==nums[k-1]):
                    continue
                i=k+1
                j=n-1
                while(i<j):
                    if(nums[i]+nums[j]+nums[k]+nums[l]==target and i!=j and j!=k and k!=l and l!=i):
                        ans.append([nums[l],nums[k],nums[i],nums[j]])
                        i+=1
                        j-=1
                        while(i<j and nums[i]==nums[i-1]):
                            i+=1
                        while(i<j and nums[j]==nums[j+1]):
                            j-=1
                    elif(nums[i]+nums[j]+nums[k]+nums[l]<target):
                        i+=1
                    else:
                        j-=1

        return ans


