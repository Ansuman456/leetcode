class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        #largest subarray with 2 unique val
        k=2
        d=dict()
        maxlen=0
        left=0
        for right in range(len(fruits)):
            d[fruits[right]]=d.get(fruits[right],0)+1
            while(len(d)>k):
                d[fruits[left]]=d.get(fruits[left])-1
                if(d[fruits[left]]==0):
                    del d[fruits[left]]
                left+=1
            maxlen=max(maxlen,right-left+1)
        return maxlen

        