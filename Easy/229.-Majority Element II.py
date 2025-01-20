Description:
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]
 

Constraints:

1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109
Python3:
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        threshold = n/3
        freq_dict = {}
        for num in nums:
            freq_dict[num] = freq_dict.get(num,0)+1
        result = [key for key, value in freq_dict.items() if value > threshold]

        return result
        
