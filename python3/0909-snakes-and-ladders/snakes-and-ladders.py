class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        length = len(board)
        board.reverse()

        def intToPos(square):
            r = (square - 1) // length
            c = (square - 1) % length
            if r % 2:
                c = length - 1 - c
            return [r, c]

        queue = deque([1])
        moves = 0
        visited = set()

        while queue:
            for _ in range(len(queue)):
                value = queue.popleft()
                for j in range(1, 7):
                    new_value = value + j

                    r, c = intToPos(new_value)

                    if board[r][c] != -1:
                        new_value = board[r][c]

                    if new_value >= len(board) ** 2:
                        return moves + 1
                    
                    if new_value not in visited:
                        queue.append(new_value)
                        visited.add(new_value)
            
            moves += 1

        return -1

