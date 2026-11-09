class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        def check(days):
            bouquets=0
            flowers=0
            for ele in bloomDay:
                if(ele<=days):
                    flowers+=1
                    if(flowers==k): #bouquets complete
                        flowers=0
                        bouquets+=1
                else: #flowers< k and ele>days
                    flowers=0
            return bouquets


        low=min(bloomDay)
        high=max(bloomDay)
        ans=-1
        while(low<=high):
            mid=low+(high-low)//2
            if(check(mid)>=m):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
