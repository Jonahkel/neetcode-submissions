class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_bits = [0]*9
        col_bits = [0]*9
        box_bits = [0]*9
        for row_idx in range(len(board)):
            for col_idx in range(len(board[0])):
                box_idx = row_idx//3*3+col_idx//3
                num = board[row_idx][col_idx]
                if num == '.': continue
                num_bit = 1 << int(num)
                if num_bit & row_bits[row_idx] or num_bit & col_bits[col_idx] or num_bit & box_bits[box_idx]:
                    return False
                row_bits[row_idx] |= num_bit
                col_bits[col_idx] |= num_bit
                box_bits[box_idx] |= num_bit

        return True