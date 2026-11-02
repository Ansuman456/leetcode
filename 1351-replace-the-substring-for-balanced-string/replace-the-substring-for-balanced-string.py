class Solution:
    def balancedString(self, s: str) -> int:
        target=len(s)/4
        d=dict()
        left=0
        count=0 #no of unbalanced char in the map
        minlen=float('inf')

        for ele in s:
            d[ele] = d.get(ele, 0) + 1
    
        for ele in d:   #count no of unbalanced char in the map
            if d[ele] > target:
                count += 1

        if(count==0):
            return 0

        #we are trying to remove/replace the window from the string and check if remaining string gets balanced
        for right in range(len(s)):
            d[s[right]]-=1 #expand 
            if(d[s[right]]==target):  #s[right] is no more unbalanced
                count-=1
            while(count==0): #string is balanced
                minlen=min(minlen,right-left+1) #store
                #shrink
                d[s[left]]+=1
                if(d[s[left]]>target): #string is unbalanced
                    count+=1
                left+=1
        return minlen

