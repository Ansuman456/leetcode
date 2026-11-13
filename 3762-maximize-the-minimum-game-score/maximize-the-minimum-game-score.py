import math
class Solution:
    def maxScore(self, points: List[int], m: int) -> int:
        def check(target):
            n = len(points)
            if n == 1:
                return math.ceil(target / points[0])
            nums = [0] * n  #nums[i] shows the no of moves taken for nums[i] to reach target
            nums[0]=1
            total_visits = 1   

            for i in range(len(points)):
                games=math.ceil(target/points[i])  # no of visits required to make nums[i] reach target
                remainingVisits=games-nums[i]
                if(i!=len(points)-1):  #not last ele
                    if(remainingVisits > 0):  #more moves required to reach target
                        nums[i]+=remainingVisits
                        nums[i+1]+=remainingVisits  # update next idx
                        total_visits += 2 * remainingVisits
                    # else dont make any more moves for nums[i]

                    if (i != n-2 or
                        nums[i+1] < math.ceil(target / points[i+1])):
                        nums[i+1] += 1
                        total_visits += 1
                else:  #last ele
                    if(remainingVisits > 0):  #more moves required to reach target
                        nums[i]+=remainingVisits
                        nums[i-1]+=remainingVisits  #update previous idx cause no next
                        total_visits += 2 * remainingVisits
                    # else dont make any more moves for nums[i]
                
                if total_visits > m:    #totalvisits=moves+1
                    return False

            return True

        low=1
        high=min(points) * (m + 1)
        ans=0
        while(low<=high):
            mid=low+(high-low)//2
            if(check(mid)): # valid min gamescore -> increase it
                ans=mid
                low=mid+1
            else:
                high=mid-1
        
        return ans

                    



        