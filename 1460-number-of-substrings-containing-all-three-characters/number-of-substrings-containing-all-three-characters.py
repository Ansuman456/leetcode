class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        d=dict()
        left=0
        n=len(s)
        count=0 
        ans=0
        for right in range(len(s)):
            d[s[right]]=d.get(s[right],0)+1
            if(d[s[right]]==1):
                count+=1
            while(count==3):
                ans+=n-right
                d[s[left]]-=1
                if(d[s[left]]==0):
                    count-=1
                left+=1
        return ans