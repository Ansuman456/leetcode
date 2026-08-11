class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        longest=""
        for t in dictionary:
            i=0
            j=0
            while(i<len(s) and j<len(t)):
                if(s[i]==t[j]):
                    j+=1  # increment only on matching
                i+=1 # increment every iteration
            if(j==len(t) and len(t)>=len(longest)):
                if(len(t)==len(longest) and longest>t): # we choose lexographically smaller
                    longest=t
                elif(len(t)>len(longest)):
                    longest=t
        return longest

