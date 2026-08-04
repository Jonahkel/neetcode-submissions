class Solution:





    def To2dIndex(self, idx, width) -> tuple[int, int]:
        return (idx // width, idx % width)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)*len(matrix[0])
        width = len(matrix[0])

        while l != r:
            m = (l+r)//2
            row, col = self.To2dIndex(m, width)
            m_val = matrix[row][col]
            if m_val < target:
                l = m+1
            else:
                r = m
        row, col = self.To2dIndex(l, width)
        if row >= len(matrix) or col >= len(matrix[0]): return False
        return matrix[row][col] == target
        