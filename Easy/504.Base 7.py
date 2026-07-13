Description:
Given an integer num, return a string of its base 7 representation.

 

Example 1:

Input: num = 100
Output: "202"
Example 2:

Input: num = -7
Output: "-10"
 

Constraints:

-107 <= num <= 107
 
Python3:
import numpy as np
class Solution:
    def convertToBase7(self, num: int) -> str:
        return '-' + np.base_repr(-num, 7) if num < 0 else np.base_repr(num, 7)
        
