class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ones=0
        left=0
        minlen=float("inf")
        window=[]
        minwindow=[]
        for right in range(len(s)):
            if(s[right]=='1'): #expand
                ones+=1
            window.append(s[right])

            while(ones==k):
                if (right-left+1 < minlen or (right-left+1 == minlen and "".join(window) < "".join(minwindow))): #shorter/equal or lexicographically smaller(if equal)
                    minlen=right-left+1
                    minwindow=window[:]

                if(s[left]=='1'):
                    ones-=1
                window.remove(s[left])
                left+=1


        return "".join(minwindow)
            
            
            