'''
sorting is not super useful since each time we pick an hour k we have to calculate total
time it takes to clear all piles

k will always be bound between 1 (slowest) and max(piles)

time complexity would be O(nlogn) and space is O(1) 

'''
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)
        res = hi

        def time_to_finish(rate: int, piles: List[int]) -> int:
            time = 0
            # round up
            for b in piles:
                time += -(-b // rate)
            return time

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            time = time_to_finish(mid, piles)

            if time <= h:
                res = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return res
        