class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances=[]
        dict1={}
        list1=[]
        for p in points:
            distances.append(p[0]**2+p[1]**2)
        print(distances)
        for i in range(len(distances)):
            dict1[tuple(points[i])]=distances[i]
        heapq.heapify(distances)
        for i in range(k):
            d=heapq.heappop(distances)
            for key in dict1:
                if(dict1[key]==d):
                    list1.append(list(key))
        return list1[:k]
        