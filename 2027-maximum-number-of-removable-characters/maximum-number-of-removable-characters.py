class Solution:
    def maximumRemovals(self, s: str, p: str, removable: list[int]) -> int:
        def isSubsequence(x,y,k):
            removed = set(removable[:k])  # ele at index needs to be removed from s
            i=0
            j=0
            while(i<len(x) and j<len(y)):
                if(i not in removed and x[i]==y[j]):
                    j+=1   # move j only when match
                i+=1
            return j==len(y)  # all char of y matched with x in a sequence

        def check(removal):
            if(isSubsequence(s,p,removal)):
                return True
            return False

        low=0
        high=len(removable)
        ans=-1
        while(low<=high):
            mid=low+(high-low)//2
            if(check(mid)==True): # valid no of removalas => increase removals
                ans=mid
                low=mid+1
            else:
                high=mid-1
        return ans
