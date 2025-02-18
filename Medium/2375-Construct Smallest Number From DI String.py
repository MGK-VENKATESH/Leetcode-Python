Description:
You are given a 0-indexed string pattern of length n consisting of the characters 'I' meaning increasing and 'D' meaning decreasing.

A 0-indexed string num of length n + 1 is created using the following conditions:

num consists of the digits '1' to '9', where each digit is used at most once.
If pattern[i] == 'I', then num[i] < num[i + 1].
If pattern[i] == 'D', then num[i] > num[i + 1].
Return the lexicographically smallest possible string num that meets the conditions.

 

Example 1:

Input: pattern = "IIIDIDDD"
Output: "123549876"
Explanation:
At indices 0, 1, 2, and 4 we must have that num[i] < num[i+1].
At indices 3, 5, 6, and 7 we must have that num[i] > num[i+1].
Some possible values of num are "245639871", "135749862", and "123849765".
It can be proven that "123549876" is the smallest possible num that meets the conditions.
Note that "123414321" is not possible because the digit '1' is used more than once.
Example 2:

Input: pattern = "DDD"
Output: "4321"
Explanation:
Some possible values of num are "9876", "7321", and "8742".
It can be proven that "4321" is the smallest possible num that meets the conditions.
 

Constraints:

1 <= pattern.length <= 8
pattern consists of only the letters 'I' and 'D'.

Python3:
class Solution:
    # Check if the current sequence matches the pattern of 'I' and 'D'
    def check(self, number_sequence: str, pattern: str) -> bool:
        for index in range(len(pattern)):
            # Ensure the sequence is in increasing order at 'I' positions
            if (
                pattern[index] == "I"
                and number_sequence[index] > number_sequence[index + 1]
            ):
                return False
            # Ensure the sequence is in decreasing order at 'D' positions
            elif (
                pattern[index] == "D"
                and number_sequence[index] < number_sequence[index + 1]
            ):
                return False
        return True

    def smallestNumber(self, pattern: str) -> str:
        pattern_length = len(pattern)

        # Generate sequence "123...n+1"
        number_sequence = "".join(
            str(num) for num in range(1, pattern_length + 2)
        )

        # Use permutations generator
        for permutation in permutations(number_sequence):
            permutation_str = "".join(permutation)
            if self.check(permutation_str, pattern):
                return permutation_str
        return ""
