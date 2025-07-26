class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        visited = set()
        movements = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        def dfs(i, j, curr):

            if curr == len(word):
                return True

            if i == len(board) or j == len(board[0]) or min(i, j) < 0 or (i, j) in visited or board[i][j] != word[curr]:
                return False
            
            visited.add((i, j))

            for d_i, d_j in movements:
                if dfs(i + d_i, j + d_j, curr + 1):
                    return True
            
            visited.remove((i, j))
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        
        return False
        
        
            

