Description:
You are given a 2D integer grid of size m x n and an integer x. In one operation, you can add x to or subtract x from any element in the grid.

A uni-value grid is a grid where all the elements of it are equal.

Return the minimum number of operations to make the grid uni-value. If it is not possible, return -1.

 

Example 1:


Input: grid = [[2,4],[6,8]], x = 2
Output: 4
Explanation: We can make every element equal to 4 by doing the following: 
- Add x to 2 once.
- Subtract x from 6 once.
- Subtract x from 8 twice.
A total of 4 operations were used.
Example 2:


Input: grid = [[1,5],[2,3]], x = 1
Output: 5
Explanation: We can make every element equal to 3.
Example 3:


Input: grid = [[1,2],[3,4]], x = 2
Output: -1
Explanation: It is impossible to make every element equal.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 105
1 <= m * n <= 105
1 <= x, grid[i][j] <= 104

Python3:
class Solution:
    def minOperations(self, grid, x):
        # Create a list to store all the numbers from the grid
        nums_array = []
        result = 0

        # Flatten the grid into nums_array
        for row in grid:
            for num in row:
                nums_array.append(num)

        # Sort nums_array in non-decreasing order to easily find the median
        nums_array.sort()

        length = len(nums_array)
        # Store the median element as the final common value
        final_common_number = nums_array[length // 2]

        # Iterate through each number in nums_array
        for number in nums_array:
            # If the remainder when divided by x is different, return -1
            if number % x != final_common_number % x:
                return -1
            # Add the number of operations required to make the current number equal to final_common_number
            result += abs(final_common_number - number) // x

        return result
