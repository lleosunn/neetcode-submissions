class Solution:
    def isValidSudoku(self, board   : List[List[str]]) -> bool:
        # check all rows, check all columns, check all sub grids
        seen = set()

        # check rows
        # for r in range(9):
        #     for c in range(9):
        #         if board[r][c] in seen:
        #             return False
        #         seen.add(board[r][c])
        #     seen = set()

        # check columns
        for c in range(9):
            for r in range(9):
                if board[r][c] in seen:
                    return False
                seen.add(board[r][c])
            seen = set()

        # check sub grids
        # we can index the sub grids
        # for subr in range(3):
        #     for subc in range(3):
        #         for i in range(3):
        #             for j in range(3):
        #                 if board[subr + i][subc + j] in seen:
        #                     return False
        #                 seen.add(board[subr + i][subc + j])
        #         seen = set()
    
        return True