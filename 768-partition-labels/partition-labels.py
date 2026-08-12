class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result=[0]
        k=0
        j=len(s)-1

        while(s[j]!=s[0] and j>result[k]-1):
            j-=1
        if(j+1>result[k]):  #expand boundary
                result[k]=j+1

        for i in range(1,len(s)):
            j=len(s)-1
            while(s[j]!=s[i] and j>result[k]-1):
                j-=1

            if(i<result[k]): #same partition
                if(j+1>result[k]):  #expand boundary
                    result[k]=j+1
            elif(i>=result[k]): # new partition
                result.append(j+1)  
                k+=1
        
        if(len(result)>=2): # more than one partition
            for i in range(len(result)-1,0,-1):
                result[i]=result[i]-result[i-1]

        return result