class TrieNode:
    def __init__(self):
        self.dictionary = {}
        self.end_of_word = False

class Trie:

    def __init__(self):
        self.root_node = TrieNode()
        

    def insert(self, word: str) -> None:

        curr = self.root_node
        
        for c in word:
            if c not in curr.dictionary:
                curr.dictionary[c] = TrieNode()
            
            curr = curr.dictionary[c]
        
        curr.end_of_word = True

    def search(self, word: str) -> bool:

        curr = self.root_node
        
        for c in word:
            if c in curr.dictionary:
                curr = curr.dictionary[c]
            else:
                return False
        
        return curr.end_of_word
        

    def startsWith(self, prefix: str) -> bool:
        
        curr = self.root_node
        
        for c in prefix:
            if c in curr.dictionary:
                curr = curr.dictionary[c]
            else:
                return False
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)