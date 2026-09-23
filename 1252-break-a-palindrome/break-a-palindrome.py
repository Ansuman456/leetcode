class Solution:
    

    def breakPalindrome(self, palindrome: str) -> str:
        def isPalindrome(s):
            i = 0
            j = len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        if(len(palindrome)==1):
            return ""


        i=0
        palindrome=list(palindrome)  
        while(palindrome[i]=='a'):  # skip a, to get first non-a char
            i+=1
            if(i==len(palindrome)):
                break

        if(i==len(palindrome)): # if all are a: aaaaa -> aaaab [case 1]
            palindrome[len(palindrome)-1]='b'

        else:   # we got first non-a char [case 2]
            val=palindrome[i]
            palindrome[i]='a' # convert that to 'a' and store the idx
            store=i
            
        if(isPalindrome(palindrome)): # aabaa -> aaaaa  [case 3]
            palindrome[store]=val  #restore the val in store: aaaaa-> aabaa
            palindrome[len(palindrome)-1]='b' #put b in last place 

        return "".join(palindrome)