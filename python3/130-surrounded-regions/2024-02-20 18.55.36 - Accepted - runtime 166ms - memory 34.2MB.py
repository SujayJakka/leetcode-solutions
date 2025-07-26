class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        visited = set()

        m = len(board)
        n = len(board[0])

        islands = []

        def dfs(coordinate, island):

            i, j = coordinate

            if not(0<=i<m and 0<=j<n and (i, j) not in visited and board[i][j] == "O"):
                return
            
            visited.add((i, j))
            island.append((i, j)) 
            dfs((i+1, j), island)
            dfs((i-1, j), island)
            dfs((i, j+1), island)
            dfs((i, j-1), island)
        
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited:
                    island = []
                    dfs((i, j), island)

                    if len(island) != 0:
                        islands.append(island)

        for island in islands:

            surrounded = True
            for coordinate in island:
                i ,j = coordinate
                if i == 0 or i == m -1 or j == 0 or j == n - 1:
                    surrounded = False
                
            if surrounded == True:
                for coordinate in island:
                    i ,j = coordinate

                    board[i][j] = "X"
        
        


        