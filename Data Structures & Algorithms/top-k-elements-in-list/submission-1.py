"""
Problem domain: Arrays/Lists and Heaps (priority queue for frequency)

Constraints:
1) Can our integer array nums be empty? How should we handle that?
Never empty, always at least 1 element

2) What happens in the case of a tie and we can only return one of them?
Answer always unique so this case wont happen / doesnt matter

3) Does the order of our output matter?
No, order is irrelevant

4) How long can nums array be and how big are numbers in the array?
at most 10000 elements in nums, numbers are -1000 <-> 1000

Proposed approach and time complexity:
1) we can create a Counter() freq map to count how many times we see each # O(n) time O(n) space
2) Iterate over elements in counter to build tuple (count, num) and push into a heap O(nlogn)
time O(n) space
3) Heappop k times from heap to build res list O(klogn) time O(k) space
K always <= n so time complexity would be O(nlogn) and space O(n)

Post problem thoughts:
Another approach we have is to sort the Counter map and then take the values of the top
K counts into a list and return that
This would be same time complexity of O(nlogn) with O(n) space

Either way, this problem tests our ability to process arrays / numbers and a way to keep track
of frequency of occurrences dynamically.
"""
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # init counter map, res array, and max_heap
        freq = Counter(nums)
        res = []
        max_heap = []

        # iterate over counter and heappush tuples into heap (NEGATE FOR MAX HEAP)
        for number, count in freq.items():
            heapq.heappush(max_heap, (-count, number))

        # heappop K times and append to res (NEGATE FOR MAX HEAP)
        for i in range(k):
            _, num = heapq.heappop(max_heap)
            res.append(num)

        return res
        