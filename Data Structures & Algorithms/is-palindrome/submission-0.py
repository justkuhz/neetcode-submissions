'''
Problem domain: strings / string processing

Constraints:
How do we handle spaces or non alphanumeric characters?
How long can the string "s" be?

Approach:
set all chars in string to lowercase and then compare against reversed string
O(n) time O(n) space
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # create new string for parsing input string
        c = ""
        for char in s:
            if char.isalnum():
                c += char.lower()

        return c == c[::-1]
        