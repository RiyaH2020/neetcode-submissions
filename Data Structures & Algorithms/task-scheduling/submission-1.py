class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dict1={}
        heap=[]
        queue=deque()
        for t in tasks:
            dict1[t]=dict1.get(t,0)+1
        for k in dict1:
            heap.append(-dict1[k])
        heapq.heapify(heap)
        time=0
        while(heap or queue):
            time+=1
            if(heap):
                count=heapq.heappop(heap)+1
                if(count):
                    queue.append([count,time+n])
            if(queue):
                if(queue[0][1]==time):
                    heapq.heappush(heap,queue.popleft()[0])
        return time
            

        return 1