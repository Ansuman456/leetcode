class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        k=3
        window=set()
        left=0
        count=0
        for right in range(len(s)): #expand
            while(s[right] in window):
                #shrink until duplicate
                window.remove(s[left])
                left+=1

            #now expansion will not cause duplicate
            window.add(s[right]) #expand calc

            if(right-left+1==k):
                if(len(window)==k): # process and store
                    count+=1
                window.remove(s[left]) #shrink calc
                left+=1  #shrink

        return count
