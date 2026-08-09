class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        x=version1.split('.')
        y=version2.split('.')
        i=0
        j=0
        while(i<len(x) and j<len(y)):
            if(int(x[i]) == int(y[j])):
                i+=1
                j+=1
            elif(int(x[i]) > int(y[j])):
                return 1
            else:
                return -1

        if(i==len(x) and j<len(y)): # if y has more digits
            while(j<len(y)):  # check non zero in remaining digits
                if(int(y[j])!=0):
                    return -1
                j+=1
            return 0

        elif(j==len(y) and i<len(x)): # if x has more digits
            while(i<len(x)): # check non zero in remaining digits
                if(int(x[i])!=0):
                    return 1
                i+=1
            return 0
        elif(i==len(x) and j==len(y)):
            return 0