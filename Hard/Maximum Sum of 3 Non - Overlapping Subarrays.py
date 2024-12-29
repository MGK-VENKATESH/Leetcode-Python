Description:
Given an integer array nums and an integer k, find three non-overlapping subarrays of length k with maximum sum and return them.

Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.

 

Example 1:

Input: nums = [1,2,1,2,6,7,5,1], k = 2
Output: [0,3,5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
Example 2:

Input: nums = [1,2,1,2,1,2,1,2,1], k = 2
Output: [0,2,4]
 

Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i] < 216
1 <= k <= floor(nums.length / 3)

Python3:
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        subarray_sum = [0] * (n - k + 1)
        current_sum = sum(nums[:k])
        
        # Calculate all k-length subarray sums
        for i in range(n - k + 1):
            if i > 0:
                current_sum += nums[i + k - 1] - nums[i - 1]
            subarray_sum[i] = current_sum
        
        # Find the best subarray index from the left
        left = [0] * len(subarray_sum)
        best = 0
        for i in range(len(subarray_sum)):
            if subarray_sum[i] > subarray_sum[best]:
                best = i
            left[i] = best
        
        # Find the best subarray index from the right
        right = [0] * len(subarray_sum)
        best = len(subarray_sum) - 1
        for i in range(len(subarray_sum) - 1, -1, -1):
            if subarray_sum[i] >= subarray_sum[best]:  # Choose lexicographically smallest
                best = i
            right[i] = best
        
        # Find the best middle index and calculate maximum sum
        max_sum = 0
        result = []
        for j in range(k, len(subarray_sum) - k):
            i, l = left[j - k], right[j + k]
            total = subarray_sum[i] + subarray_sum[j] + subarray_sum[l]
            if total > max_sum:
                max_sum = total
                result = [i, j, l]
        
        return result
