Description:
Given an array nums of distinct positive integers, return the number of tuples (a, b, c, d) such that a * b = c * d where a, b, c, and d are elements of nums, and a != b != c != d.

 

Example 1:

Input: nums = [2,3,4,6]
Output: 8
Explanation: There are 8 valid tuples:
(2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
(3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)
Example 2:

Input: nums = [1,2,4,5,10]
Output: 16
Explanation: There are 16 valid tuples:
(1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
(2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
(2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,5,4)
(4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 104
All elements in nums are distinct.

Python3:
from collections import defaultdict
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:


        product_map = defaultdict(int)
        n = len(nums)
        count = 0

        # Step 1: Compute all product pairs
        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                product_map[product] += 1  # Count occurrences of this product

        # Step 2: Count valid tuples
        for product in product_map:
            k = product_map[product]
            if k > 1:  # At least two pairs exist
                count += (k * (k - 1)) // 2 * 8  # Combinations * 8

        return count
