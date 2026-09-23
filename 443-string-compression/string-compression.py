class Solution:
    def compress(self, chars: List[str]) -> int:
        read=0
        write=0
        count=0
        s=[]
        for read in range(len(chars)):
            if(read==0):
                count=1
                continue
            if(chars[read]==chars[read-1]):
                count+=1 # on repeat increase count
            else:
                s.append(chars[read-1])  # on new element store state of previous char 
                if count > 1:
                    s.extend(str(count)) # we extend instead of append because count string can have multiple digit, each digit should be added separately.
                count=1 # on new char reset count
        
        # for the last char
        s.append(chars[-1])
        if count > 1:
            s.extend(str(count))

        chars[:] = s
        return len(chars)