class Solution:
    def isValidSudoku(self, board   : List[List[str]]) -> bool:
        # check all rows, check all columns, check all sub grids
        seen = set()

        # check rows
        for r in range(9):
            for c in range(9):
                if board[r][c] in seen:
                    return False
                if board[r][c] != ".":
                    seen.add(board[r][c])
            seen = set()

        # check columns
        for c in range(9):
            for r in range(9):
                if board[r][c] in seen:
                    return False
                if board[r][c] != ".":
                    seen.add(board[r][c])
            seen = set()

        # check sub grids
        # we can index the sub grids
        for subr in range(3):
            for subc in range(3):
                for i in range(3):
                    for j in range(3):
                        if board[subr * 3 + i][subc * 3 + j] in seen:
                            return False
                        if board[subr * 3 + i][subc * 3 + j] != ".":
                            seen.add(board[subr * 3 + i][subc * 3 + j])
                seen = set()
    
        return True