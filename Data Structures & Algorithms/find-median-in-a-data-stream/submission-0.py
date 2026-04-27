class MedianFinder:

    def __init__(self):
        self.list1=[]
        

    def addNum(self, num: int) -> None:
        self.list1.append(num)
        

    def findMedian(self) -> float:
        self.list1.sort()
        n=len(self.list1)
        if(n==1):
            return self.list1[0]
        if(n%2!=0):
            return self.list1[n//2]
        else:
            return ((self.list1[n//2-1]+self.list1[n//2])/2)
        
        