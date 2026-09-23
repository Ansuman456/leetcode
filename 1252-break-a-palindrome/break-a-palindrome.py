class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if(len(palindrome)==1):
            return ""
        
        palindrome=list(palindrome)
        n=len(palindrome)
        for i in range(0,n//2): #[case 1]
            if(palindrome[i]!='a'):
                palindrome[i]='a'
                return "".join(palindrome)
        
        #[case 2 and 3]
        palindrome[n-1]='b'
        return "".join(palindrome)

