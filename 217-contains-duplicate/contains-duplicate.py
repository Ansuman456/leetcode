class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d={}
        for ele in nums:
            if ele in  d:
                return True
            else:
                d[ele]=1
        return False     