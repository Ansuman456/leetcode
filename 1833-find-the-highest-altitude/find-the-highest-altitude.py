class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        prefixSum=0
        highestAlt=0
        for i in range(len(gain)):
            prefixSum+=gain[i]
            highestAlt=max(highestAlt,prefixSum)
        
        return highestAlt