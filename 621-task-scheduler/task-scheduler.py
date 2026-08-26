from collections import Counter, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequency = Counter(tasks)
        max_heap =[]
        for point in frequency.values():
            heapq.heappush(max_heap, -point)
        print(max_heap)
        
        cooldown = deque()
        time = 0
        while max_heap or cooldown:
            if cooldown and cooldown[0][0] <= time:
                available_time, remaining_count = cooldown.popleft()
                heapq.heappush(max_heap,remaining_count)

            if max_heap:
                remaining = heapq.heappop(max_heap)
                remaining +=1 
                if remaining != 0:
                    available_time = time + n + 1
                    cooldown.append((available_time, remaining))
            
            time += 1

        return time