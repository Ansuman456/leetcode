class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def check(x):
            left=index
            right=n-index-1

            p=min(left,x-1)
            q=max(0,left-(x-1))
            leftsum=(p*x)-(p*(p+1)//2)+q

            p=min(right,x-1)
            q=max(0,right-(x-1))
            rightsum=(p*x)-(p*(p+1)//2)+q

            return leftsum+x+rightsum
        
        low=1
        high=maxSum
        ans=-1
        while(low<=high):
            mid=low+(high-low)//2
            if(check(mid)<=maxSum): # valid sum, increase x(nums[index])
                ans=mid
                low=mid+1
            else:   # invalid sum, decrease x 
                high=mid-1
        
        return ans

