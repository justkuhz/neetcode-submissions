'''
problem domain: stack, lists, sorting

approach and complexity:
i think to find an optimal solution we should sort the array by pairing position and speed and
sorting in a way to have our positions descending to see which cars are closes to target first

for each car we should computer the time it takes to reach the target, push the time onto
a stack.

we check if a new cars time is <= the time before it, and if it catches up and joins the fleet
we should pop it from the stack

the number of remaining times in the stack equals the number of fleets

Time is O(nlogn) and space is O(n)

key insight:
whether a car joins a fleet or is a unique fleet is based on the amount of time it takes for
a particular car to reach the destination. this means we can use a stack to keep track of this
by popping/skipping cars that are part of the same fleet and only holding on to cars that
are a start of a new fleet
'''
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # init stack
        stack = []

        # create a list of pairs
        pairs = [(p, s) for p, s in zip(position, speed)]

        # sort descending
        pairs.sort(reverse=True)

        # iterate over pairs
        for p, s in pairs:
            # append time it takes to reach destination to stack
            stack.append((target - p) / s)
            # check if we have a prev element for comparison
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        # return length of stack / number of fleets
        return len(stack)
        