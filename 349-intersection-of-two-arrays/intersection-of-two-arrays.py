class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i=0
        j=0
        k=0
        result=[]
        while(i<len(nums1) and j<len(nums2)):
            if(nums1[i]==nums2[j]):
                if(k==0):
                    result.append(nums1[i])
                    k+=1
                elif(result[k-1]!=nums1[i]):
                    result.append(nums1[i])
                    k+=1
                i+=1
                j+=1
                
            elif(nums1[i]<nums2[j]): # keep larger one, move smaller one so that in future more intersections possible dont miss out
                i+=1
            else:
                j+=1
        
        return result

        