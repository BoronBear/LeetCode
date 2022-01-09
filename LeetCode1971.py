from typing import List
class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        tree_connect = [i for i in range(n)]
        for edge in edges:
            v1, v2 = edge[0], edge[1]
            while tree_connect[v1] != v1:
                v1 = tree_connect[v1]
            while tree_connect[v2] != v2:
                v2 = tree_connect[v2]
            tree_connect[v1] = v2
        g1, g2 = start, end
        while tree_connect[g1] != g1:
            g1 = tree_connect[g1]
        while tree_connect[g2] != g2:
            g2 = tree_connect[g2]
        return (g1 == g2)