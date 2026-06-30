'''
Problem domain: Sliding windows / hash maps / lists

Constraints: Can s be empty? Can k be greater than s?
s is 1 <= 1000 and k is 0 <= len(s)

Approach and complexity:
We can use a frequency map to keep count of each char and sliding window to evaluate if
a window is a valid substring or not
O(n) time and O(26) space
'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # init freq map, result, left ptr, max freq
        count = defaultdict(int)
        res = 0
        l = 0
        max_freq = 0

        # iterate over len(s)
        for r in range(len(s)):
            # update freq of s[r]
            count[s[r]] += 1

            # update max_freq with highest freq seen so far
            max_freq = max(max_freq, count[s[r]])

            # if tracked condition is violated we shrink window and adjust count
            while (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1

            # update result
            res = max(res, r - l + 1)

        # return res
        return res


        

        