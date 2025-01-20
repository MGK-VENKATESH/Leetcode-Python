Description:
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
 
Constraints:
The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104
 
Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

Python3:
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # In-order traversal (iterative or recursive)
        def in_order_traversal(node):
            if not node:
                return []
            # Combine left subtree, root, and right subtree
            return in_order_traversal(node.left) + [node.val] + in_order_traversal(node.right)
        
        # Get sorted elements using in-order traversal
        sorted_elements = in_order_traversal(root)
        
        # Return the kth smallest element (1-indexed)
        return sorted_elements[k - 1]
