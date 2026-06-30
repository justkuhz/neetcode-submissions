'''
Constraints:
Can s be empty? What should we return in this case?
s can be empty and we should return 0

What characters can be in s?
any ASCII

Key insights:
we can solve this in one pass using a sliding window

Approach and complexity:
Sliding window + hash set
The moment we see a duplicate character we slide our left ptr and remove characters from hash
set until we pass the duplicated character

O(n) time and O(m) space where m is number of unique characters
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # init ptrs and res + map
        l, r = 0, 0
        res = 0
        char_set = set()

        # iterate over s
        while r < len(s):
            # check if its a duplicate
            if s[r] in char_set:
                
                # slide left ptr
                while s[l] != s[r]:
                    char_set.remove(s[l])
                    l += 1
                l += 1

            # update map
            char_set.add(s[r])
            
            # update result (if applicable)
            res = max(res, r - l + 1)
            
            # move r up
            r += 1

        return res


        