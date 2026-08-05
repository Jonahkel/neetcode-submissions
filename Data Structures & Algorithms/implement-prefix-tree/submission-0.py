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
            next_node = curr.children[self.to_idx(char)]
            if next_node is None:
                break
            curr = next_node
            let_idx += 1
        while let_idx < len(word):
            char = word[let_idx]
            next_node = Node()
            curr.children[self.to_idx(char)] = next_node
            curr = next_node
            let_idx += 1
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
        