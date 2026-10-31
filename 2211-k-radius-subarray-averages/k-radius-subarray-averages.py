class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        result=[]
        for i in range(len(nums)):
            result.append(-1)
        
        left=0
        sum=0
        x=2*k+1
        for right in range(len(nums)): #expand
            sum+=nums[right] #expand calc

            if(right-left+1==x): #write avg in middle of window
                #process and store
                avg=sum//x
                mid=left+k
                result[mid]=avg

                #shrink calc
                sum-=nums[left] 
                left+=1 #shrink
        return result

