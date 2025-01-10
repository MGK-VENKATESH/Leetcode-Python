Description:
You are given two string arrays words1 and words2.

A string b is a subset of string a if every letter in b occurs in a including multiplicity.

For example, "wrr" is a subset of "warrior" but is not a subset of "world".
A string a from words1 is universal if for every string b in words2, b is a subset of a.

Return an array of all the universal strings in words1. You may return the answer in any order.

 

Example 1:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
Output: ["facebook","google","leetcode"]
Example 2:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]
Output: ["apple","google","leetcode"]
 

Constraints:

1 <= words1.length, words2.length <= 104
1 <= words1[i].length, words2[i].length <= 10
words1[i] and words2[i] consist only of lowercase English letters.
All the strings of words1 are unique.
Python3:
from collections import Counter

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # Step 1: Get the frequency count for words in words2
        max_freq = Counter()
        
        # For each word in words2, update the maximum frequency required for each character
        for word in words2:
            word_freq = Counter(word)
            for char, count in word_freq.items():
                max_freq[char] = max(max_freq[char], count)
        
        # Step 2: Check each word in words1
        result = []
        for word in words1:
            word_freq = Counter(word)
            # Check if word contains all the required characters with sufficient frequency
            if all(word_freq[char] >= max_freq[char] for char in max_freq):
                result.append(word)
        
        return result
