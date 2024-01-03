class Trie:
    def __init__(self) -> None:
        self.children = {}
        self.endWord = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        res = set()

        nodeThing = Trie()

        for word in words:
            temp = nodeThing
            for c in word:
                if c not in temp.children:
                    temp.children[c] = Trie()
                temp = temp.children[c]
            temp.endWord = True
        

        def dfs(i, j, parent, thing):

            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
                return
    
            if board[i][j] == "#" or board[i][j] not in parent.children:
                return
            
            currNode = parent.children[board[i][j]]
            thing += board[i][j]

            if currNode.endWord == True:
                res.add(thing)
            
            original = board[i][j]
            board[i][j] = "#"

            dfs(i+1, j, currNode, thing) 
            dfs(i-1, j, currNode, thing) 
            dfs(i, j+1, currNode, thing) 
            dfs(i, j-1, currNode, thing)
            
            board[i][j] = original

            if not currNode.children:
                parent.children.pop(original)
                
            return
        
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, nodeThing, "")
        return res
