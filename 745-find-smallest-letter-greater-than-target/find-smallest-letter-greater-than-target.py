class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        low=0
        high=len(letters)-1
        position=-1

        while(low<=high):
            mid=low+(high - low)//2
            if letters[mid] <= target:
                low = mid + 1
            else:
                position=mid
                high = mid - 1
        
        if(position==-1):
            return letters[0]
        return letters[position]   