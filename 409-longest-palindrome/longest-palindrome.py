class Solution:
    def longestPalindrome(self, s: str) -> int:
        d={}
        oddfreq=0 #no of odd freq characters
        for ele in s:
            d[ele]=0
        for ele in s:
            d[ele]+=1
            if(d[ele]%2!=0): #on first occurance cosider that oddfreq
                oddfreq+=1
            else: # on 2nd occurance remove that from oddfreq
                oddfreq-=1
        if(oddfreq==0): #no oddfreq, all even freq
            return len(s)
        else: # include one odd freq char as middle of palindrome
            return len(s)-oddfreq+1