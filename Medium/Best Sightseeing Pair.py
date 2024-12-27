Description:
You are given an integer array values where values[i] represents the value of the ith sightseeing spot. Two sightseeing spots i and j have a distance j - i between them.

The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j: the sum of the values of the sightseeing spots, minus the distance between them.

Return the maximum score of a pair of sightseeing spots.

 

Example 1:

Input: values = [8,1,5,2,6]
Output: 11
Explanation: i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11
Example 2:

Input: values = [1,2]
Output: 2

Python3:
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_values_plus_i = values[0]  # Initial value of values[i] + i
        max_score = 0  # To store the maximum score
        
        for j in range(1, len(values)):
            # Calculate the score for the pair (i, j)
            max_score = max(max_score, max_values_plus_i + values[j] - j)
            # Update max_values_plus_i for the next iteration
            max_values_plus_i = max(max_values_plus_i, values[j] + j)
        
        return max_score
