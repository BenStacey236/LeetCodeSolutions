# Medium Problem
# Problem 208


class TrieNode:

    def __init__(self):
        self.branches: dict[str, TrieNode] = {}
        self.wordEnd: bool = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        
        node = self.root
        for letter in word:
            if letter not in node.branches:
                node.branches[letter] = TrieNode()
            
            node = node.branches[letter]

        node.wordEnd = True
        

    def search(self, word: str) -> bool:

        node = self.root
        for letter in word:
            if letter not in node.branches:
                return False

            node = node.branches[letter]
        
        return node.wordEnd
        

    def startsWith(self, prefix: str) -> bool:

        node = self.root
        for letter in prefix:
            if letter not in node.branches:
                return False

            node = node.branches[letter]
        
        return True