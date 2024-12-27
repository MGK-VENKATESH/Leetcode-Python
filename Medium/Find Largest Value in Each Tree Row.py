Description:
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

 

Example 1:


Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]
Example 2:

Input: root = [1,2,3]
Output: [1,3]
 

Constraints:

The number of nodes in the tree will be in the range [0, 104].
-231 <= Node.val <= 231 - 1

Python3:
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        queue = deque([root])  # Queue for level-order traversal

        while queue:
            level_size = len(queue)
            max_value = float('-inf')  # Initialize max for this level

            for _ in range(level_size):
                node = queue.popleft()
                max_value = max(max_value, node.val)  # Update max value for this level

                if node.left:
                    queue.append(node.left)  # Add left child to queue
                if node.right:
                    queue.append(node.right)  # Add right child to queue

            result.append(max_value)  # Add the max value for this level to the result

        return result
