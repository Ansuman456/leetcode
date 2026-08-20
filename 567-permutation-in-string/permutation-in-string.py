class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d={}
        count=0
        #fill the dictionary with p
        for ele in s1:
            if(ele in d):
                d[ele]+=1
            else:
                d[ele]=1
                count+=1
       
        left=0
        k=len(s1)
        for right in range(len(s2)):
            if(s2[right] in d):
                d[s2[right]]-=1 #expand
                if(d[s2[right]]==0):
                    count-=1

            if(right-left+1==k):
                #store before shrinking
                if(count==0):
                    return True
                #shrink
                if(s2[left] in d):
                    d[s2[left]]+=1 #doing reverse(increase instead of decrease)
                    if(d[s2[left]]==1):
                        count+=1
                left+=1
        
        return False