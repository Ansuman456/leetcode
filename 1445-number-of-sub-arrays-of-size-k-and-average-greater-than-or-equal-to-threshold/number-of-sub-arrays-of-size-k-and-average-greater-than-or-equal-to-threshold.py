class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left=0
        n=len(arr)
        ans=0
        sum=0 # window
        for right in range(len(arr)):
            sum+=arr[right] #expand

            if(right-left+1==k): #works after high>=k
                avg=sum/k
                if(avg>=threshold):
                    ans+=1

                sum-=arr[left] # shrink
                left+=1
        return ans