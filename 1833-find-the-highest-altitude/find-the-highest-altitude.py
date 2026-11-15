class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        prefixSum=[0]*(len(gain)+1)
        prefixSum[0]=0
        highestAlt=0
        for i in range(len(gain)):
            prefixSum[i+1]=prefixSum[i]+gain[i]
            highestAlt=max(highestAlt,prefixSum[i+1])
        
        return highestAlt