class Solution:
    def longestPalindrome(self, s: str) -> int:
        d={}
        oddfreq=0
        for ele in s:
            d[ele]=0
        for ele in s:
            d[ele]+=1
            if(d[ele]%2!=0):
                oddfreq+=1
            else:
                oddfreq-=1
        if(oddfreq==0):
            return len(s)
        else:
            return len(s)-oddfreq+1