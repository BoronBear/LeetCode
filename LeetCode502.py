from typing import List
import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        curr_capital = w
        explored_projects = []
        unexplored_projects = sorted(list(zip(capital, profits)), reverse=True)

        for proj_num in range(k):  # choose projects one at a time
            while unexplored_projects and unexplored_projects[-1][0] <= curr_capital:
                heapq.heappush(explored_projects, -unexplored_projects.pop()[1])

            if explored_projects:
                selected_p = heapq.heappop(explored_projects)
                curr_capital -= selected_p

        return curr_capital

