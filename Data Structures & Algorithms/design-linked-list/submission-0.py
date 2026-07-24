class Node:
    def __init__(self, val):
        self.val = val
        self.right: Node|None = None
        self.left:Node|None = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        if index not in range(self.length) or self.head is None: return -1
        idx = 0
        cur = self.head
        while idx < index and cur.right is not None:
            cur = cur.right
            idx += 1
        return cur.val

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.right = self.head
        if newNode.right is not None:
            newNode.right.left = newNode
        else:
            self.tail = newNode
        self.head = newNode
        self.length += 1

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        newNode.left = self.tail
        if newNode.left is not None:
            newNode.left.right = newNode
        else:
            self.head = newNode
        self.tail = newNode
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index not in range(0, self.length+1): return
        newNode = Node(val)
        idx = 0
        curr = self.head
        prev = None
        while idx < index and curr is not None:
            prev = curr
            curr = curr.right
            idx += 1
        if prev is None:
            self.head = newNode
        if curr is None:
            self.tail = newNode
        newNode.left = prev
        newNode.right = curr
        if prev is not None:
            prev.right = newNode
        if curr is not None:
            curr.left = newNode
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index not in range(0, self.length): return
        idx = 0
        curr = self.head
        prev = None
        while idx < index and curr is not None:
            prev = curr
            curr = curr.right
            idx += 1
        if curr is not None:
            after = curr.right
        if prev is not None:
            prev.right = after
        else:
            self.head = after
        if after is not None:
            after.left = prev
        else:
            self.tail = prev
        
        self.length -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)