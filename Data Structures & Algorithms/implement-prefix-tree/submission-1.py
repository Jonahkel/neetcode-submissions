class Node:
    def __init__(self) -> None:
        self.end = False
        self.children: list[Node | None] = [None] * 26

class PrefixTree:

    def __init__(self):
        self.root: Node = Node()

    def to_idx(self, char):
        return ord(char) - ord('a')

    def insert(self, word: str) -> None:
        curr = self.root
        let_idx = 0
        while let_idx < len(word):
            char = word[let_idx]
            if curr.children[self.to_idx(char)] is None:
                curr.children[self.to_idx(char)] = Node()
            curr = curr.children[self.to_idx(char)]
            let_idx += 1
            if curr is None: return
        curr.end = True
        
        
    def search(self, word: str) -> bool:
        let_idx = 0
        curr = self.root
        while let_idx < len(word):
            curr = curr.children[self.to_idx(word[let_idx])]
            if curr is None: return False
            let_idx += 1
        return curr.end
        

    def startsWith(self, prefix: str) -> bool:
        let_idx = 0
        curr = self.root
        while let_idx < len(prefix):
            curr = curr.children[self.to_idx(prefix[let_idx])]
            if curr is None: return False
            let_idx += 1
        return True
        