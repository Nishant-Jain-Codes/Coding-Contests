class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        weaker = set()
        for team in grid: 
            for i,j in enumerate(team):
                if j == 1:
                    weaker.add(i)
        for i in range(len(grid)):
            if i not in weaker:
                return i
        return -1
                
        