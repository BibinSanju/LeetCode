class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        in_deg = [0] * n
        for u,v in edges:
            in_deg[v] += 1
        
        return list(i for i in range(n) if in_deg[i] == 0)
