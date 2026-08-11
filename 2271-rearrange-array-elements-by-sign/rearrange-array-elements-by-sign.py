class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result=[]
        read=0
        write1=0 # keeps positive
        write2=1 # keeps positive
        for ele in nums:  # fill result array
            result.append(ele)

        while(write1<len(result) or write2<len(result)):
            if(nums[read]>=0):
                result[write1]=nums[read]
                write1+=2
                read+=1
            else:
                result[write2]=nums[read]
                write2+=2
                read+=1
        return result
            
            