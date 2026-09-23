class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for arr in image:
            i=0
            j=len(arr)-1
            
            while(i<=j):
                # for reversing
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp

                # dont invert i and j both causing double invert when i=j
                if(i!=j):
                    #invert i
                    if(arr[i]==0):
                        arr[i]=1
                    else:
                        arr[i]=0
                    #invert j
                    if(arr[j]==0):
                        arr[j]=1
                    else:
                        arr[j]=0

                # i and j are pointing to same middle element       
                else: # invert any one: i or j -> in my case it's [i]
                    if(arr[i]==0):
                        arr[i]=1
                    else:
                        arr[i]=0
                i+=1
                j-=1

        return image
            