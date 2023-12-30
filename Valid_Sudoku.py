class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        notFilled = []


        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] not in rows[i]:
                        rows[i].add(board[i][j])
                    else:
                        return False

                    if board[i][j] not in cols[j]:
                        cols[j].add(board[i][j])
                    else:
                        return False
       
                    square = 3 * (i // 3) + (j // 3)
                    if board[i][j] not in squares[square]:
                        squares[square].add(board[i][j])
                    else:
                        return False

        return True


