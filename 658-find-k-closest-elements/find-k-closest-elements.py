class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # find ciel or floar of x using binary search (lets say ciel) 
        # then use 2 pointers to expand the list of k values(outwards from middle)

        low=0
        high=len(arr)-1
        ciel=0
        while(low<=high):
            mid=low+(high-low)//2
            if(arr[mid]>=x):  # search in left for ciel
                high=mid-1
            else:
                low=mid+1
    # at the end of loop, low points x or its ciel
        
        j=low
        i=j-1
        count=k  
        ans=[]
        while count > 0:
            if i < 0:  #i pointer reached end
                ans.append(arr[j])
                j += 1
            elif j >= len(arr):  #j pointer reached end
                ans.append(arr[i])
                i -= 1

            elif abs(arr[i] - x) <= abs(arr[j] - x):
                ans.append(arr[i])
                i -= 1
            else:
                ans.append(arr[j])
                j += 1

            count -= 1

        ans.sort()
        return ans
            
            






