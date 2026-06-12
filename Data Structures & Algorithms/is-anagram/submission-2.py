"""
how long are the strings?
max 50000 chars long

what kind of characters are in the string?
only lowercase english letters

can the strings be different lengths or are they the same length?
they dont have to be same length

easy edge case:
if strings are different lengths they are not an anagram

2 approaches:
1) we can use two freq arrays of size 26 to calculate number of times we see each char
and compare them, this lets us reduce space complexity to O(1), but this only works in the 
case that they are lower case english letters or upper case english letters

2) we can use a freq map Counter() for each word and compare them, space is O(n) but suitable
in case input is beyond english lowercase letters

Both of these approaches are O(n) time

post problem thoughts:
This problem falls under arrays since we need to be comfortable treating the strings 
as if they are an array of chars and iterate/process over them to evaluate some condition(s)
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_count = [0] * 26
        t_count = [0] * 26

        for char in s:
            s_count[ord(char) - ord('a')] += 1
        
        for char in t:
            t_count[ord(char) - ord('a')] += 1

        return s_count == t_count