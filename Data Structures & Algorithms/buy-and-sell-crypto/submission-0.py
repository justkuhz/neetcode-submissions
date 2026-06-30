'''
Problem domain: lists / pointers / sliding window

Constraints:
Can we have negative prices? What is the min/max value of prices?
Prices at minimum is 0 and max is 100

Can prices be empty? How long can prices be?
At least 1 price, up to 100 elements

Approach:
We can solve this in one pass using a sliding window, two ptrs that find each window where we
have an increasing run
We will reset the window whenever we read a new minimum and keep track of a max profit that
we recalculate whenever we expand our window
O(n) time O(1) space

Key insight:
We only care about `windows` of elements in our list that are relatively increasing, we can use
a left pointer to track a relative minimum and expand to see what our profits look like
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # init pointers and trackers
        l, r = 0, 0
        res = 0

        # pass over array
        while r < len(prices) - 1:
            # check if we slide left or right pointer
            if prices[r + 1] > prices[l]:
                r += 1
                profit = prices[r] - prices[l]
                res = max(res, profit)
            else:
                l = r + 1
                r = l
        
        return res

        