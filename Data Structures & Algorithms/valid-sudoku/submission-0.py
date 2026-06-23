'''
we can use hash sets to check if our cols, rows, and 3x3 sub-grids are
valid.

Problem domain falls under arrays/list/matrix processing

Constraints:
1) Are the values in the array guaranteed to be integers between 1-9?
Strings are either "." for empty or "1" - "9"
2) How are empty spaces in the board displayed?
see above
'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = (r / 3, c / 3)

        for r in range(9):
            for c in range(9):
                # skip empty spot
                if board[r][c] == ".":
                    continue

                # check for duplicates across col/row/square
                if (board[r][c] in rows[r] or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                
                # add num to hash sets
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        # never saw duplicate / false
        return True
        
        