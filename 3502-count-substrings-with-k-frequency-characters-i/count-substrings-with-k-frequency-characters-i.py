class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        left=0
        maxcount=0
        ans=0
        d=dict()
        n=len(s)
        for right in range(len(s)):
            d[s[right]]=d.get(s[right],0)+1
            maxcount=max(maxcount, d[s[right]])   # trace the max count in the map
            while(maxcount>=k):
                ans+=n-right
                d[s[left]]-=1
                if(d[s[left]]==0):
                    del d[s[left]]
                #update maxcount if we have removed the maxchar one
                if(d.get(s[left],0)+1==maxcount):
                    maxcount=max(d.values(),default=0) #defualt 0 if map is empty
                left+=1
        return ans

