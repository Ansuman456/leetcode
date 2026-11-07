class Solution:
    def mySqrt(self, x: int) -> int:
        low=1
        high=x
        while(low<=high):
            mid=low+(high-low)//2
            if(mid*mid==x):
                return mid
            elif(mid*mid<x):
                low=mid+1
            else:
                high=mid-1
        return high   #roundoff to previous integer after crossing
 