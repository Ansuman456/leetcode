class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        tno=0
        fno=0
        left=0
        maxlen=0
        for right in range(len(answerKey)):
            if(answerKey[right]=='T'):
                tno+=1
            else:
                fno+=1
            while(tno>k and fno>k):
                if(answerKey[left]=='T'):
                    tno-=1
                else:
                    fno-=1
                left+=1
            maxlen=max(maxlen,right-left+1)
        return maxlen
        