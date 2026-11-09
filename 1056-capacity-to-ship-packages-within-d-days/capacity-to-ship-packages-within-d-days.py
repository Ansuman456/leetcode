class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def check(capacity):
            d=1  # to ship any package atleast 1 day required
            add=0
            for ele in weights:
                if(add+ele>capacity):
                    d+=1
                    add=0
                add+=ele
            return d
                

        low=max(weights)
        high=sum(weights)
        ans=-1
        while(low<=high):
            mid=low+(high-low)//2

            if(check(mid)<=days):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
