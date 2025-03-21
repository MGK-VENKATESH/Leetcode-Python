Description:
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
 

Constraints:

0 <= rowIndex <= 33
 
Python3:
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # Start with the first row
        row = [1]
        
        for i in range(rowIndex):
            # Generate the next row using the previous row
            # Add 0 at the end and the beginning, and compute the sum
            row = [x + y for x, y in zip([0] + row, row + [0])]
        
        return row
