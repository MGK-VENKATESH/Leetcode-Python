Description:
You are given an integer array nums and two integers minK and maxK.

A fixed-bound subarray of nums is a subarray that satisfies the following conditions:

The minimum value in the subarray is equal to minK.
The maximum value in the subarray is equal to maxK.
Return the number of fixed-bound subarrays.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
Output: 2
Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].
Example 2:

Input: nums = [1,1,1,1], minK = 1, maxK = 1
Output: 10
Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.
 

Constraints:

2 <= nums.length <= 105
1 <= nums[i], minK, maxK <= 106

Python3:
class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        count = 0
        left = 0
        dq_min = deque()
        dq_max = deque()
        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                dq_min.clear()
                dq_max.clear()
                left = i + 1
                continue
            while dq_min and nums[dq_min[-1]] >= nums[i]:
                dq_min.pop()
            dq_min.append(i)
            while dq_max and nums[dq_max[-1]] <= nums[i]:
                dq_max.pop()
            dq_max.append(i)
            if nums[dq_min[0]] == minK and nums[dq_max[0]] == maxK:
                start = min(dq_min[0], dq_max[0])
                count += (start - left + 1)
        return count
