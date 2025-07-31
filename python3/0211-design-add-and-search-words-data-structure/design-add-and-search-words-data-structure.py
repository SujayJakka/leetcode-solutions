class TrieNode:

    def __init__(self):
        self.dictionary = {}
        self.end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.dictionary:
                curr.dictionary[c] = TrieNode()
            curr = curr.dictionary[c]
            
        curr.end_of_word = True
        
    def search(self, word: str) -> bool:

        def dfs(node, index):
            if len(word) == index:
                return node.end_of_word
            
            if word[index] == ".":
                for c in node.dictionary:
                    if dfs(node.dictionary[c], index + 1):
                        return True
            elif word[index] in node.dictionary:
                if dfs(node.dictionary[word[index]], index + 1):
                    return True
                
            return False
        
        return dfs(self.root, 0)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)