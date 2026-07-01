'''
Problem domain: sliding window, hash maps, lists, strings

Constraints:
Can s1 or s2 be empty?
No, both guaranteed at least 1 element

Can s1 be longer than s2? How long can both strings be?
Yes, s1 can be longer than s2. Both from 1 <= 1000

Are either strings limited in the characters they can contain?
No

Easy edge case:
Return false if s1 is longer than s2

Approach and complexity:
Create a freq hashmap / char count of s1
Create sliding window of len(s1) on s2
Keep track of char map as we slide the window
Return true if the char map for s2 window at any point is == char map of s1

Time complexity O(n + m) where n = len(s1) and m = len(s2)
Space complexity O(n + m)
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # edge case
        if len(s1) > len(s2):
            return False
        
        # build char maps
        char_s1 = Counter(s1)
        char_s2 = Counter(s2[:len(s1)])

        # set ptrs
        l = 0
        r = len(s1) - 1
        while r < len(s2):
            # check for match
            if char_s1 == char_s2:
                return True
            
            # shift window and update map
            char_s2[s2[l]] -= 1
            l += 1
            r += 1
            if r == len(s2):
                break
                
            char_s2[s2[r]] += 1

        # last check
            if char_s1 == char_s2:
                return True

        return False

        