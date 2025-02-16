Description:
Given an integer n, find a sequence that satisfies all of the following:

The integer 1 occurs once in the sequence.
Each integer between 2 and n occurs twice in the sequence.
For every integer i between 2 and n, the distance between the two occurrences of i is exactly i.
The distance between two numbers on the sequence, a[i] and a[j], is the absolute difference of their indices, |j - i|.

Return the lexicographically largest sequence. It is guaranteed that under the given constraints, there is always a solution.

A sequence a is lexicographically larger than a sequence b (of the same length) if in the first position where a and b differ, sequence a has a number greater than the corresponding number in b. For example, [0,1,9,0] is lexicographically larger than [0,1,5,6] because the first position they differ is at the third number, and 9 is greater than 5.

 

Example 1:

Input: n = 3
Output: [3,1,2,3,2]
Explanation: [2,3,2,1,3] is also a valid sequence, but [3,1,2,3,2] is the lexicographically largest valid sequence.
Example 2:

Input: n = 5
Output: [5,3,1,4,3,5,2,4,2]
 

Constraints:

1 <= n <= 20


Python3:
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        len_seq = 2 * n - 1 # 1 occurs once, 2-n appear twice
        seq = [0] * len_seq # init with empty vals
        used = set() # tracks nums used in seq

        def backtrack(i):
            if i == len_seq: return True # filled all of sequence
            if seq[i]: return backtrack(i + 1) # already filled index, check next

            for num in range(n, 0, -1): # try using num at index, n to 1 for lexicographically largest seq
                if num in used: continue # already used num in sequence

                nxt = i + num if num > 1 else i # second occurance of num, nxt = i if num = 1 so 1 occurance

                if nxt >= len_seq or seq[nxt] != 0: continue # invalid second index
                
                seq[i] = seq[nxt] = num # set two occurances of num
                used.add(num)

                if backtrack(i + 1): # try to fill rest of sequence
                    return True

                seq[i] = seq[nxt] = 0 # couldn't fill rest, reset seq
                used.remove(num)

            return False # no num option lead to valid sequence

        backtrack(0) # start backtrack at 0 index
        return seq 
