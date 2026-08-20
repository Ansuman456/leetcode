class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        right=len(cardPoints)-1
        ans=0
        add=0
        for left in range(k):
            add+=cardPoints[left]
            ans=max(ans,add)
        add-=cardPoints[left]
        left-=1

# now we do sliding window backwards
        while(right>=len(cardPoints)-k):
            # expand
            add+=cardPoints[right]

            #store before shrink
            ans=max(ans,add)
            #shrink
            add-=cardPoints[left]
            left-=1

            right-=1

        return ans
        


