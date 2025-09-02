import heapq

class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
    
        def gain(p, t):
            return (float(p+1)/(t+1)) - (float(p)/t)
        heap = [(-gain(p, t), p, t) for p, t in classes]
        heapq.heapify(heap)
        for _ in range(extraStudents):
            g, p, t = heapq.heappop(heap)
            p, t = p+1, t+1  
            heapq.heappush(heap, (-gain(p, t), p, t))
        total = 0.0
        while heap:
            _, p, t = heapq.heappop(heap)
            total += float(p) / t

        return total / len(classes)
