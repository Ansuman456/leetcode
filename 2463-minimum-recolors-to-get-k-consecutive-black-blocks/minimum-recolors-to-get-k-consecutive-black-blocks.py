class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left=0
        ans=200
        white=0
        for right in range(len(blocks)):
            if(blocks[right]=='W'): # expand
                white+=1
            
            if(right-left+1==k):
                #store before shrinking
                ans=min(ans,white)
                #shrink
                if(blocks[left]=='W'):
                    white-=1
                left+=1
        
        return ans