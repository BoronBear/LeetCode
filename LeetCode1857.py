from typing import List

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:

        n = len(colors)

        # Only use the colors we need instead of 26.
        color_dict = {}
        color_count = 0
        for c in colors:
            if c not in color_dict:
                color_dict[c] = color_count
                color_count += 1
        int_colors = []
        for c in colors:
            int_colors.append(color_dict[c])

        # adjacency list
        out_vertices = [[] for i in range(n)]
        in_counts = [0 for i in range(n)]
        cur_vset = []
        next_vset = []

        # initialize adjacency list
        for edge in edges:
            out_vertices[edge[0]].append(edge[1])
            in_counts[edge[1]] += 1

        for i in range(len(in_counts)):
            if in_counts[i] == 0:
                cur_vset.append(i)

        color_counts = [[0 for i in range(color_count)] for j in range(n)]
        iteration = 1

        # initial set with no in-edges
        for v in cur_vset:
            color_counts[v][int_colors[v]] = 1

        # max n times, more implies a loop
        while (iteration <= n) and (len(cur_vset) != 0):
            for v in cur_vset:
                # for each out-vertex of our current iteration, update max color-counts w/ lookahead
                for out_v in out_vertices[v]:
                    for i in range(color_count):
                        color_counts[out_v][i] = max(color_counts[out_v][i],
                                                     color_counts[v][i] + (int_colors[out_v] == i))
                    in_counts[out_v] -= 1
                    if (in_counts[out_v] == 0) and (out_v not in next_vset):
                        next_vset.append(out_v)
            cur_vset = next_vset
            next_vset = []
            iteration += 1

        if sum(in_counts) > 0:
            return -1

        else:
            max_value = 0
            for count in color_counts:
                max_value = max(max_value, max(count))
            return max_value

