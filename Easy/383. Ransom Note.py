Description:
Given two strings ransomNote and magazine, return true if ransomNote is constructed by using the letter from magazine and false otherwise.

Each letter in magazine can be used once in ransomNote.

Example1: 
Input: ransomNote = "a"  magazine = "b"
output: false


Example2:
Input: ransomNote = "aa"   magazine = "ab"
output: false

Example3:
Input: ransomNote = "aa"     magazine = "aab"
output: true

Constraints:
1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consists of lowercase english letters


Python3:
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dictionary = {}
        for ch in magazine:
            if ch not in dictionary:
                dictionary[ch] = 1
            else:
                dictionary[ch] += 1
        for ch in ransomNote:
            if ch in dictionary and dictionary[ch] > 0:
                dictionary[ch] -= 1
            else:
                return False
        return True        
