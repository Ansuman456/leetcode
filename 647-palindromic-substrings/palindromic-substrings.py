class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(s,l,r):
            while(l>=0 and r<len(s) and s[l]==s[r]):
                l-=1
                r+=1
            return r-l-1
        count=0
        for i in range(len(s)):
            #odd
            odd=expand(s,i,i)
            count += (odd + 1) // 2 # adding all odd palindrom
            #even
            if(i>0): # for i=0 we cant do i-1
                even=expand(s,i-1,i)
                count += even // 2  # adding all even palindrom
        return count