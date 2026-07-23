class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        box_sets = [set() for _ in range(9)]
        for row_idx in range(len(board)):
            for col_idx in range(len(board[0])):
                box_idx = row_idx//3*3+col_idx//3
                num = board[row_idx][col_idx]
                if num == '.': continue
                if num in row_sets[row_idx] or num in col_sets[col_idx] or num in box_sets[box_idx]:
                    return False
                row_sets[row_idx].add(num)
                col_sets[col_idx].add(num)
                box_sets[box_idx].add(num)
        return True