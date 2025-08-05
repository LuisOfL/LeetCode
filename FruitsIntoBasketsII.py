class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        n = len(fruits)
        used = [False] * n  
        notPlaced = 0      

        for i in range(n): 
            placed = False
            for j in range(n): 
                if not used[j] and baskets[j] >= fruits[i]:
                    used[j] = True  
                    placed = True
                    break
            if not placed:
                notPlaced += 1  
        return notPlaced
