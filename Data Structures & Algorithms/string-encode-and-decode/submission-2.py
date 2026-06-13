class Solution:

    def encode(self, strs: List[str]) -> str:
        # result string
        res = ""
        # length indicator + delimiter
        for string in strs:
            # eg ["example", "string"] = 7#example6#string
            res += str(len(string)) + "#" + string
        
        return res

    def decode(self, s: str) -> List[str]:
        # result array and pointer
        res = []
        i = 0
        
        # iterate char by char over encoded string
        while i < len(s):
            # find char length and delimiter
            j = i
            # find pound character
            while s[j] != "#":
                j += 1
            # transform length into integer
            length = int(s[i:j])
            # substring appended to res
            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        
        return res