class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.list1=nums
        

    def add(self, val: int) -> int:
        self.list1.append(val)
        self.list1.sort()
        n=len(self.list1)
        return self.list1[n-self.k]

        
