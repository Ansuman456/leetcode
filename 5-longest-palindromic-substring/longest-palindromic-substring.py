class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(s,l,r):
            while(l>=0 and r<len(s) and s[l]==s[r]):
                l-=1
                r+=1
            return [l,r]
        
        if(len(s)==1):
            return s

        longest=""
        for i in range(0,len(s)):
            #odd
            odd=expand(s,i,i)
            n=odd[1]-odd[0]-1
            if(n>len(longest)):
                longest=s[odd[0]+1:odd[1]]
            
            #even
            if(i>0): # for i=0 we cant do i-1
                even=expand(s,i-1,i)
                n=even[1]-even[0]-1
                if(n>len(longest)):
                    longest=s[even[0]+1:even[1]]
        return longest

