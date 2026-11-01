class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d=dict()
        left=0
        maxlen=0
        maxfreq=0
        for right in range(len(s)):
            #expand
            d[s[right]]=d.get(s[right],0)+1
            maxfreq=max(maxfreq,d[s[right]])
            while((right-left+1)-maxfreq>k): #shrink
                d[s[left]]=d.get(s[left])-1
                maxfreq=max(d.values())
                left+=1
            #process and store
            maxlen=max(maxlen,right-left+1)
        return maxlen
                
