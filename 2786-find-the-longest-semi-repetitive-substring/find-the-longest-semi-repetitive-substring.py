class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        equalpair=0
        pairs=[]
        left=0
        maxlen=0
        for right in range(len(s)):
            if(right>0 and s[right]==s[right-1]): 
                equalpair+=1 # incr no of adjacent equal pair
                pairs.append(right) #store idx of 2nd char of adjacent equal pair
            while(pairs and pairs[0]>left and equalpair>1): # shrink till last adjacent equal pair is removed from window
                if(left==pairs[0]-1): #first char of last adjacent equal pair
                    pairs.pop(0) #remove last adjacent equal pair from pairs list 
                    equalpair-=1 # remove last adjacent equal pair from no of equalpair
                left+=1
            maxlen=max(maxlen,right-left+1)
        return maxlen

