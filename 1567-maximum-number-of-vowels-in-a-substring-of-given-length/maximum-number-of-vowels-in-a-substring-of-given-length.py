class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left=0
        ans=0
        count=0
        for right in range(len(s)):
            if(s[right] in 'aeiou'):
                count+=1
            
            if(right-left+1==k):
                #store before shrinking
                ans=max(ans,count)
                #shrink
                if(s[left] in 'aeiou'):
                    count-=1
                left+=1
            
        return ans