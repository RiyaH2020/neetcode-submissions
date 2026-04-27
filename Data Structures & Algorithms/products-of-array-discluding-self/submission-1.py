class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod1=1
        prod2=1
        count_zero=0
        list1=[]
        for n in nums:
            if(n==0):
                count_zero+=1

            if(n!=0):
                prod1=prod1*n
            prod2=prod2*n
        for n in nums:
            if(n==0):
                list1.append(prod1)
            else:
                list1.append(prod2//n)
        if count_zero>=2:
            for i in range(len(list1)):
                list1[i]=0
        return list1
        
        