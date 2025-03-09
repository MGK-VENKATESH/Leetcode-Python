Description:
There is a circle of red and blue tiles. You are given an array of integers colors and an integer k. The color of tile i is represented by colors[i]:

colors[i] == 0 means that tile i is red.
colors[i] == 1 means that tile i is blue.
An alternating group is every k contiguous tiles in the circle with alternating colors (each tile in the group except the first and last one has a different color from its left and right tiles).

Return the number of alternating groups.

Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.

 

Example 1:

Input: colors = [0,1,0,1,0], k = 3

Output: 3

Explanation:



Alternating groups:



Example 2:

Input: colors = [0,1,0,0,1,0,1], k = 6

Output: 2

Explanation:



Alternating groups:



Example 3:

Input: colors = [1,1,0,1], k = 4

Output: 0

Explanation:



 

Constraints:

3 <= colors.length <= 105
0 <= colors[i] <= 1
3 <= k <= colors.length

Python3:
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        # Extend the array to handle circular sequences
        for i in range(k - 1):
            colors.append(colors[i])

        length = len(colors)
        result = 0
        # Initialize the bounds of the sliding window
        left = 0
        right = 1

        while right < length:
            # Check if the current color is the same as the last one
            if colors[right] == colors[right - 1]:

                # Pattern breaks, reset window from the current position
                left = right
                right += 1
                continue

            # Extend window
            right += 1

            # Skip counting sequence if its length is less than k
            if right - left < k:
                continue

            # Record a valid sequence and shrink window from the left to search for more
            result += 1
            left += 1

        return result
