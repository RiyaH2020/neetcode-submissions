class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dict1={}
        heap=[]
        queue=deque()
        for t in tasks:
            if(t in dict1):
                dict1[t]+=1
            else:
                dict1[t]=1
        for t in dict1:
            heap.append(-dict1[t])
        heapq.heapify(heap)

        time=0
        while heap or queue:
            time+=1
            if(heap):
                count=1+heapq.heappop(heap)
                if(count):
                    queue.append([count,time+n])
            if(queue and queue[0][1]==time):
                heapq.heappush(heap,queue.popleft()[0])
        return time





        
        



        
    

            


        