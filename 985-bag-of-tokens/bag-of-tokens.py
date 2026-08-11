class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        i=0
        j=len(tokens)-1
        score=0
        ans=0
        if(len(tokens)==0): #when there is no ele
            return 0
        if(power<tokens[i]): #when there is 1 ele
            return 0
        while(i<=j):
            if(tokens[i]<=power):
                power-=tokens[i]
                score+=1  # increase as many score by loosing power greedily
                ans=max(ans,score) # track max score in whole operation
                i+=1
            elif(score>0):
                power+=tokens[j]  #increase maximum power with loosing 1 score
                score-=1
                j-=1
        return ans
            