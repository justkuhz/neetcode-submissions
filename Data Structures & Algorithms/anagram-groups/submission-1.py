'''
Problem domain is arrays, strings, and hashmap

Constraints: 
1) Are there any constraints on the characters that can make up a string?
lower case english letters

2) Can we have an empry strs array input?
no, at least 1 element/value in the list

3) How long are strings in array strs?
max 100 chars long

4) How long can array strs be?
max 1000 stings inside of array strs

5) Can we have empty strings in strs? how do we process them?
empty strings should return an empty string in the output

Proposed approach and time complexity:
We can use a hashmap with key:value of string:List[str]. One pass iterate over array strs
and sort each string to get a key for that string and append or insert into the map.

if we call max string length in strs as "w" and "n" for number of elements in strs, our 
time complexity would be O(n*wlog(w)) with space complexity of O(n)

Post problem thoughts:
This problem requires a good understanding of how to use hash maps and how to iterate over
lists and hashmap values to produce a result.

This approach works well in the case that our strings are not limited to lowercase english
letters. If we know we are only able to intake lower case english letters instead of sorting
we can also build a tuple of a 26 size character freq array to use as the map key for O(n) 
time instead of O(n*wlog(w)).
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # init map and res list
        anagrams = defaultdict(list)
        res = []

        # iterate over strs
        for string in strs:
            # build char freq map
            count = [0] * 26
            for char in string:
                count[ord(char) - ord('a')] += 1

            # append into map
            if tuple(count) in anagrams:
                anagrams[tuple(count)].append(string)
            else:
                anagrams[tuple(count)] = [string]

        # iterate over values in map and append to res
        for group in anagrams.values():
            res.append(group)

        return res
        