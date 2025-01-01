Description:
Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

 

Example 1:

Input: s = "011101"
Output: 5 
Explanation: 
All possible ways of splitting s into two non-empty substrings are:
left = "0" and right = "11101", score = 1 + 4 = 5 
left = "01" and right = "1101", score = 1 + 3 = 4 
left = "011" and right = "101", score = 1 + 2 = 3 
left = "0111" and right = "01", score = 1 + 1 = 2 
left = "01110" and right = "1", score = 2 + 1 = 3
Example 2:

Input: s = "00111"
Output: 5
Explanation: When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5
Example 3:

Input: s = "1111"
Output: 3
 

Constraints:

2 <= s.length <= 500
The string s consists of characters '0' and '1' only.

Python3:
class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        # Precompute prefix sums for the count of '1's
        total_ones = s.count('1')
        
        max_score = 0
        left_zeros = 0
        right_ones = total_ones
        
        # Iterate through valid split points
        for i in range(n - 1):  # Split must leave non-empty substrings
            if s[i] == '0':
                left_zeros += 1
            else:
                right_ones -= 1
            
            # Update the maximum score
            max_score = max(max_score, left_zeros + right_ones)
        
        return max_score
