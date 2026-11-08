class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        low=0
        high=len(letters)

        while(low<high):
            mid=low+(high - low)//2
            if letters[mid] > target:
                high = mid
            else:
                low = mid + 1
        return letters[low % len(letters)]