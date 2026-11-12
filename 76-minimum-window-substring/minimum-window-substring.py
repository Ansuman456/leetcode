class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left=0
        d=dict()
        window=[]
        minlen = float('inf')
        ans=[]
        for ele in t:
            if(ele in d):
                d[ele]+=1
            else:
                d[ele]=1
        count=len(d) #no of nonzero freq char in map
        for right in range(len(s)):
            #expand
            window.append(s[right])
            if(s[right] in d):
                d[s[right]]-=1
                if(d[s[right]]==0):
                    count-=1
            #got answer
            while(count==0): 
                if(len(window)<minlen):
                    minlen = len(window)
                    ans = s[left:right+1]
                        
                if(s[left] in d and d[s[left]]<0): #extra char
                    d[s[left]]+=1
                elif(s[left] in d and d[s[left]]==0): #not extra but char in the map going out of the window
                    d[s[left]] += 1  # now d[s[left]]=1
                    count += 1 # now count is no longer 0, d[s[left]]>0
                window.remove(s[left])
                left+=1
        return "".join(ans)



            