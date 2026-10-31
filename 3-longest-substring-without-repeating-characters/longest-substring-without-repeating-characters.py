class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        longest=0
        window=set()
        for right in range(len(s)):
            #while invalid -> shrink
            while(s[right] in window):
                window.remove(s[left])
                left+=1
            window.add(s[right]) #expand calc
            #store
            longest=max(longest,len(window))
        
        return longest
           
            

            