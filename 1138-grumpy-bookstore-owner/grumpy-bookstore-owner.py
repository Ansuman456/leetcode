class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        left=0
        ans=0
        unsatisfied=0  # we are finding most unsatisfied customers in any window
        for right in range(len(customers)):
            if(grumpy[right]==1): #add into unsatisfied 
                unsatisfied+=customers[right]       
            #shrink
            if(right-left+1==minutes):
                # store before shrinking
                ans=max(ans,unsatisfied)
                #shrinking
                if(grumpy[left]==1):
                    unsatisfied-=customers[left]
                left+=1

        # now ans contains most unsatisfied customers window
        for i in range(len(customers)):
            if(grumpy[i]==0):
                ans+=customers[i]

        return ans


