class DoubleUnion:
    def __init__(self) -> None:
        self.left_edge = {}
        self.right_edge = {}
        self.longest = 0

    def find(self, num:int, edge:dict):
        root = edge[num]
        temp = num
        while root != temp:
            temp = root
            root = edge[root]
        
        temp = num
        while root != temp:
            num = edge[num]
            edge[temp] = root
            temp = num
        
        return root
    
            
    def insert(self, num:int):
        if num in self.left_edge or num in self.right_edge: return
        if num-1 in self.left_edge:
            self.left_edge[num] = self.find(num-1, self.left_edge)
        else:
            self.left_edge[num] = num
        if num+1 in self.right_edge:
            self.right_edge[num] = self.find(num+1, self.right_edge)
        else:
            self.right_edge[num] = num
        self.right_edge[self.left_edge[num]] = self.right_edge[num]
        self.left_edge[self.right_edge[num]] = self.left_edge[num]
        self.longest = max(self.longest, self.right_edge[num] - self.left_edge[num]+1)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        du = DoubleUnion()
        for num in nums:
            du.insert(num)
        print(du.left_edge)
        print(du.right_edge)
        return du.longest

