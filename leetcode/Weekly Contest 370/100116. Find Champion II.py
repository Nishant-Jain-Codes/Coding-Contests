class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        isWeaker = [False]*n
        # print(isWeaker)
        for i,edge in enumerate(edges):
            # print(edge)
            ui=edge[0]
            vi=edge[1]
            isWeaker[vi]=True
        strongCount = 0
        strongVal = -1
        for i,weak in enumerate(isWeaker):
            if not weak:
                strongVal = i
                strongCount+=1
        if strongCount == 1:
            return strongVal
        else:
            return -1