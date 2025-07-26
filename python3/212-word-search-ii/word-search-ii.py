class TrieNode:
    def __init__(self):
        self.children = defaultdict(lambda: None)
        self.word = None
    def add(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Create Trie with existing words
        root = TrieNode()

        for word in words:
            root.add(word)
        
        res = set()
        visited = set()
        ROWS, COLS = len(board), len(board[0])

        def dfs(i, j, node):
            if min(i, j) < 0 or i == ROWS or j == COLS or (i,j) in visited or board[i][j] not in node.children:
                return
            
            node = node.children[board[i][j]]
            
            if node.word:
                res.add(node.word)
            
            visited.add((i, j))
            dfs(i + 1, j, node)
            dfs(i - 1, j, node)
            dfs(i, j + 1, node)
            dfs(i, j - 1, node)
            visited.remove((i, j))

        for i in range(ROWS):
            for j in range(COLS):
                dfs(i, j, root)
                if len(res) == len(words):
                    return list(res)
        return list(res)