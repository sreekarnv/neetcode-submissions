class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        boxes = collections.defaultdict(set)
        
        for i in range(9):
            for j in range(9):
                curr = board[i][j]

                if curr == ".":
                    continue
                
                idx = i // 3, j // 3
                if curr in cols[i] or curr in rows[j] or curr in boxes[idx]:
                    return False
                
                cols[i].add(curr)
                rows[j].add(curr)
                boxes[idx].add(curr)
        
        return True
