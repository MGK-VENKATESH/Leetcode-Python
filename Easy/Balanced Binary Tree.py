Description:
Given a binary tree, determine if it is 
height-balanced
.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104

Python3:
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Helper function to compute the height of a subtree
        def height(node):
            if not node:
                return 0  # An empty subtree has height 0
            
            # Recursively find the height of left and right subtrees
            left_height = height(node.left)
            right_height = height(node.right)
            
            # If a subtree is unbalanced, propagate -1 upwards
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1
            
            # Return the height of the current node
            return max(left_height, right_height) + 1
        
        # The tree is balanced if height does not return -1
        return height(root) != -1
