'''
key-value store = hashmap
key = string, value = List[(int, "string")]
key insight is that we will append new values to the list and the integers will be sorted
when we try to get a value with a timestamp, we want the exact timestamp or the most recent
one if an exact does not exist
returns empty string if there are no values with the key requested

timemap init is O(1) time 
set is O(1) time
get is O(logn) time

space is O(n*m) where n is number of keys and m is the max number of times we update the value
of a key (append / increase length of value list)
'''
class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        pair = (timestamp, value)
        if key not in self.store:
            self.store[key] = [(pair)]
        else:
            self.store[key].append(pair)


    def get(self, key: str, timestamp: int) -> str:
        # retrieve list from map and init ptrs
        res, values = "", self.store.get(key, [])
        l, r = 0, len(values) - 1

        # search values
        while l <= r:
            mid = l + (r - l) // 2

            # if we are at a new possible candidate for exact or recent
            if values[mid][0] <= timestamp:
                res = values[mid][1]
                l = mid + 1
            else:
                r = mid - 1

        return res

        
