Description:
You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:

A land cell if grid[r][c] = 0, or
A water cell containing grid[r][c] fish, if grid[r][c] > 0.
A fisher can start at any water cell (r, c) and can do the following operations any number of times:

Catch all the fish at cell (r, c), or
Move to any adjacent water cell.
Return the maximum number of fish the fisher can catch if he chooses his starting cell optimally, or 0 if no water cell exists.

An adjacent cell of the cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) or (r - 1, c) if it exists.

 

Example 1:


Input: grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
Output: 7
Explanation: The fisher can start at cell (1,3) and collect 3 fish, then move to cell (2,3) and collect 4 fish.
Example 2:


Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]
Output: 1
Explanation: The fisher can start at cells (0,0) or (3,3) and collect a single fish. 
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
0 <= grid[i][j] <= 10

Python3:
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0 or (row, col) in visited:
                return 0
            
            visited.add((row, col))
            
            res = 0
            for direction in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                res += dfs(row + direction[0], col + direction[1])
            
            return res + grid[row][col]
        
        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] > 0 and (i, j) not in visited:
                    res = max(res, dfs(i, j))

        return res
