class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left=0
        maxlen=0
        cost=0
        for right in range(len(s)):
            cost+=abs(ord(s[right])-ord(t[right]))
            while(cost>maxCost):
                cost-=abs(ord(s[left])-ord(t[left]))
                left+=1
            if(cost<=maxCost):
                maxlen=max(maxlen,right-left+1)
        
        return maxlen