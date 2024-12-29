Description:
There exist two undirected trees with n and m nodes, numbered from 0 to n - 1 and from 0 to m - 1, respectively. You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1, respectively, where edges1[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the first tree and edges2[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the second tree.

You must connect one node from the first tree with another node from the second tree with an edge.

Return the minimum possible diameter of the resulting tree.

The diameter of a tree is the length of the longest path between any two nodes in the tree.

 

Example 1:

Input: edges1 = [[0,1],[0,2],[0,3]], edges2 = [[0,1]]

Output: 3

Explanation:

We can obtain a tree of diameter 3 by connecting node 0 from the first tree with any node from the second tree.

Example 2:


Input: edges1 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]], edges2 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]]

Output: 5

Explanation:

We can obtain a tree of diameter 5 by connecting node 0 from the first tree with node 0 from the second tree.

 

Constraints:

1 <= n, m <= 105
edges1.length == n - 1
edges2.length == m - 1
edges1[i].length == edges2[i].length == 2
edges1[i] = [ai, bi]
0 <= ai, bi < n
edges2[i] = [ui, vi]
0 <= ui, vi < m
The input is generated such that edges1 and edges2 represent valid trees.
Python3:
from collections import defaultdict, deque

class Solution:
    def minimumDiameterAfterMerge(self, edges1, edges2):
        # Helper function to find tree diameter using BFS
        def find_diameter(edges, n):
            # Build adjacency list
            graph = defaultdict(list)
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)
            
            # BFS to find the farthest node
            def bfs(start):
                dist = [-1] * n
                dist[start] = 0
                q = deque([start])
                farthest_node = start
                while q:
                    node = q.popleft()
                    for neighbor in graph[node]:
                        if dist[neighbor] == -1:
                            dist[neighbor] = dist[node] + 1
                            q.append(neighbor)
                            farthest_node = neighbor
                return farthest_node, dist[farthest_node]
            
            # First BFS to find one endpoint of the diameter
            node1, _ = bfs(0)
            # Second BFS to find the diameter length
            _, diameter = bfs(node1)
            return diameter
        
        # Number of nodes in each tree
        n = len(edges1) + 1
        m = len(edges2) + 1
        
        # Find diameters of both trees
        diameter1 = find_diameter(edges1, n)
        diameter2 = find_diameter(edges2, m)
        
        # Compute minimum diameter after merging
        min_diameter = max(diameter1, diameter2, (diameter1 + 1) // 2 + 1 + (diameter2 + 1) // 2)
        return min_diameter
