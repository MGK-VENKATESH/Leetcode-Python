Description:
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false
 
Constraints:
The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
 Follow up: Could you solve it both recursively and iteratively?

Python3:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
            if not t1 and not t2:
                return True
            # If only one node is None, or their values differ, they are not symmetric
            if not t1 or not t2 or t1.val != t2.val:
                return False
            # Check the left subtree of t1 with the right subtree of t2, and vice versa
            return isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)
        
        # Start the symmetry check with the left and right children of the root
        return isMirror(root.left, root.right) if root else True
