class Solution:
    def arrangeCoins(self, n: int) -> int:
        # linear appoach, decrement n by i in loop[lets say n to x] and each time check if next stair is possible (O(i))   -> 1,3,6,10.....
        # in binary approach we dont traverse from n to x in loop by 1.  find a no whose n*(n+1)/2 is lower bound of N (<=n) for values of k(stair no)
        def sumOfFirstX(x):
            return x*(x+1)/2

        low=1
        high=n
        ans=-1
        while(low<=high):
            mid=low+(high-low)//2
            if(sumOfFirstX(mid)<=n): #search in right
                ans=mid
                low=mid+1
            else:
                high = mid - 1;          
        return ans

