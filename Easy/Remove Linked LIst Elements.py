Description:
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

 

Example 1:


Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
Example 2:

Input: head = [], val = 1
Output: []
Example 3:

Input: head = [7,7,7,7], val = 7
Output: []
 

Constraints:

The number of nodes in the list is in the range [0, 104].
1 <= Node.val <= 50
0 <= val <= 50
Python3:
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Create a dummy node to handle edge cases like removing the head node
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        # Traverse the list
        while current.next:
            if current.next.val == val:
                # Remove the node by skipping it
                current.next = current.next.next
            else:
                # Move to the next node
                current = current.next
        
        # Return the new head
        return dummy.next
