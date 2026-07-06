Description:
Given two integers a and b, return the sum of the two integers without using the operators + and -.

 

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = 2, b = 3
Output: 5
 

Constraints:

-1000 <= a, b <= 1000
 

Python3:
class Solution(object):
    def getSum(self, a, b):
        a &= 0xffffffff
        b &= 0xffffffff
        while b:
            c = (a & b) << 1
            a = (a ^ b) & 0xffffffff
            b = c & 0xffffffff
        return a if a < 0x80000000 else ~(a ^ 0xffffffff)
