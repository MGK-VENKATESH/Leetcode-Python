Description:
Given a string s and an integer k, return true if you can use all the characters in s to construct k palindrome strings or false otherwise.

 

Example 1:

Input: s = "annabelle", k = 2
Output: true
Explanation: You can construct two palindromes using all characters in s.
Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"
Example 2:

Input: s = "leetcode", k = 3
Output: false
Explanation: It is impossible to construct 3 palindromes using all the characters of s.
Example 3:

Input: s = "true", k = 4
Output: true
Explanation: The only possible solution is to put each character in a separate string.
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= 105

Python3:
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # If k is greater than the length of the string, it's impossible to form k palindromes
        if k > len(s):
            return False
        
        # Count the frequency of each character
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Count the number of characters with odd frequencies
        odd_count = sum(1 for count in char_count.values() if count % 2 != 0)
        
        # We can form k palindromes if the number of odd frequencies is less than or equal to k
        return odd_count <= k
