Description:
You are given a positive integer days representing the total number of days an employee is available for work (starting from day 1). You are also given a 2D array meetings of size n where, meetings[i] = [start_i, end_i] represents the starting and ending days of meeting i (inclusive).

Return the count of days when the employee is available for work but no meetings are scheduled.

Note: The meetings may overlap.

 

Example 1:

Input: days = 10, meetings = [[5,7],[1,3],[9,10]]

Output: 2

Explanation:

There is no meeting scheduled on the 4th and 8th days.

Example 2:

Input: days = 5, meetings = [[2,4],[1,3]]

Output: 1

Explanation:

There is no meeting scheduled on the 5th day.

Example 3:

Input: days = 6, meetings = [[1,6]]

Output: 0

Explanation:

Meetings are scheduled for all working days.

 

Constraints:

1 <= days <= 109
1 <= meetings.length <= 105
meetings[i].length == 2
1 <= meetings[i][0] <= meetings[i][1] <= days

Python3:
class Solution:
    def countDays(self, days: int, meetings: list[list[int]]) -> int:
        day_map = defaultdict(int)
        prefix_sum = 0
        free_days = 0
        previous_day = days
        has_gap = False

        for meeting in meetings:
            # Set first day of meetings
            previous_day = min(previous_day, meeting[0])

            # Process start and end of meeting
            day_map[meeting[0]] += 1
            day_map[meeting[1] + 1] -= 1

        # Add all days before the first day of meetings
        free_days += previous_day - 1
        for current_day in sorted(day_map.keys()):
            # Add current range of days without a meeting
            if prefix_sum == 0:
                free_days += current_day - previous_day
            prefix_sum += day_map[current_day]
            previous_day = current_day

        # Add all days after the last day of meetings
        free_days += days - previous_day + 1
        return free_days
