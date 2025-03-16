Description:
You are given an integer array ranks representing the ranks of some mechanics. ranksi is the rank of the ith mechanic. A mechanic with a rank r can repair n cars in r * n2 minutes.

You are also given an integer cars representing the total number of cars waiting in the garage to be repaired.

Return the minimum time taken to repair all the cars.

Note: All the mechanics can repair the cars simultaneously.

 

Example 1:

Input: ranks = [4,2,3,1], cars = 10
Output: 16
Explanation: 
- The first mechanic will repair two cars. The time required is 4 * 2 * 2 = 16 minutes.
- The second mechanic will repair two cars. The time required is 2 * 2 * 2 = 8 minutes.
- The third mechanic will repair two cars. The time required is 3 * 2 * 2 = 12 minutes.
- The fourth mechanic will repair four cars. The time required is 1 * 4 * 4 = 16 minutes.
It can be proved that the cars cannot be repaired in less than 16 minutes.​​​​​
Example 2:

Input: ranks = [5,1,8], cars = 6
Output: 16
Explanation: 
- The first mechanic will repair one car. The time required is 5 * 1 * 1 = 5 minutes.
- The second mechanic will repair four cars. The time required is 1 * 4 * 4 = 16 minutes.
- The third mechanic will repair one car. The time required is 8 * 1 * 1 = 8 minutes.
It can be proved that the cars cannot be repaired in less than 16 minutes.​​​​​
 

Constraints:

1 <= ranks.length <= 105
1 <= ranks[i] <= 100
1 <= cars <= 106
Python3:
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        min_rank, max_rank = ranks[0], ranks[0]

        # Find min and max rank dynamically
        for rank in ranks:
            min_rank = min(min_rank, rank)
            max_rank = max(max_rank, rank)

        # Frequency list to count mechanics with each rank
        freq = [0] * (max_rank + 1)
        for rank in ranks:
            min_rank = min(min_rank, rank)
            freq[rank] += 1

        # Minimum possible time, Maximum possible time
        low = 1
        high = min_rank * cars * cars

        # Perform binary search to find the minimum time required
        while low < high:
            mid = (low + high) // 2
            cars_repaired = 0

            # Calculate the total number of cars that can be repaired in 'mid' time
            for rank in range(1, max_rank + 1):
                cars_repaired += freq[rank] * int(math.sqrt(mid // rank))

            # Adjust the search boundaries based on the number of cars repaired
            if cars_repaired >= cars:
                high = mid  # Try to find a smaller time
            else:
                low = mid + 1  # Need more time

        return low
