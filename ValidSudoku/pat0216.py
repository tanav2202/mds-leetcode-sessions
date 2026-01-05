class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dot = "."
       
        
        count =0
        for row in range(9):
            rowset = set()
            for col in range(9):
                if board[row][col] != dot:
                    if board[row][col] in rowset:
                        print("mistake in rowset")
                        return False
                    else:
                        count+=1
                        print(count)
                        rowset.add(board[row][col])
                
                
        
        for col in range(9):
            colset = set()
            for row in range(9):
                if board[row][col] != dot:
                    if board[row][col] in colset:
                        print("mistake in colset")
                        return False
                    else:
                        colset.add(board[row][col])
        
       
        count =0
        for block_row in range(0,9,3):
            
            for block_col in range(0,9,3):
                blockset = set()
                for row in range(3):
                    
                    
                    for col in range(3):  
                        count +=1
                        print(count)
                        if board[block_row+row][block_col+col] != dot:
                            if board[row+block_row][col+block_col] in blockset:
                                return False
                            else:
                                blockset.add(board[row+block_row][col+block_col])
                        
                        
        return True
                
