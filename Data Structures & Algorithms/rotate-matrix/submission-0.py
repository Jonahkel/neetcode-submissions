class Solution:

    def point_rotations(self, r, c, matrix):
        return [(c, len(matrix)-1-r), (len(matrix)-1-r, len(matrix)-1-c), (len(matrix)-1-c, r),  (r,c)]


    def rotate(self, matrix: List[List[int]]) -> None:
        for layer in range (len(matrix) // 2):
            for top_idx in range(layer,len(matrix)-layer-1):
                num = matrix[layer][top_idx]
                for row, col in self.point_rotations(layer, top_idx, matrix):
                    temp = num
                    num = matrix[row][col]
                    matrix[row][col] = temp
        
