Description:
You are given a 0-indexed integer array arr, and an m x n integer matrix mat. arr and mat both contain all the integers in the range [1, m * n].

Go through each index i in arr starting from index 0 and paint the cell in mat containing the integer arr[i].

Return the smallest index i at which either a row or a column will be completely painted in mat.

 

Example 1:

image explanation for example 1
Input: arr = [1,3,4,2], mat = [[1,4],[2,3]]
Output: 2
Explanation: The moves are shown in order, and both the first row and second column of the matrix become fully painted at arr[2].
Example 2:

image explanation for example 2
Input: arr = [2,8,7,4,1,3,5,6,9], mat = [[3,2,5],[1,4,6],[8,7,9]]
Output: 3
Explanation: The second column becomes fully painted at arr[3].
 

Constraints:

m == mat.length
n = mat[i].length
arr.length == m * n
1 <= m, n <= 105
1 <= m * n <= 105
1 <= arr[i], mat[r][c] <= m * n
All the integers of arr are unique.
All the integers of mat are unique.

Python3:
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])  # Dimensions of the matrix
        
        # Map each number to its (row, column) position in the matrix
        pos = {}
        for r in range(m):
            for c in range(n):
                pos[mat[r][c]] = (r, c)
        
        # Arrays to track painted rows and columns
        row_count = [0] * m
        col_count = [0] * n
        
        # Process each number in arr
        for i, num in enumerate(arr):
            row, col = pos[num]
            
            # Paint the cell
            row_count[row] += 1
            col_count[col] += 1
            
            # Check if this row or column is completely painted
            if row_count[row] == n or col_count[col] == m:
                return i
        
        # Should never reach here based on the problem constraints
        return -1
