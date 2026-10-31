class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        d={}
        count=0
        #fill the dictionary with p
        for ele in p:
            if(ele in d):
                d[ele]+=1
            else:
                d[ele]=1
                count+=1
       
        left=0
        ans=[]
        k=len(p)
        for right in range(len(s)):
            if(s[right] in d): 
                d[s[right]]-=1 #expand(decrease freq from dic)
                if(d[s[right]]==0):
                    count-=1

            if(right-left+1==k):
                #store before shrinking
                if(count==0): #the widow is an anagram
                    ans.append(left)
                #shrink
                if(s[left] in d):
                    d[s[left]]+=1 #doing reverse(increase instead of decrease)(increase freq from dic)
                    if(d[s[left]]==1):
                        count+=1
                left+=1
        
        return ans

