class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dot = "."
        i_dict = {}
        block_dict = {}
        j_dict = {}
        for i in range(0,9):
            
            for j in range(0,9):
                
                block_i = i//3
                block_j = j//3
                block_num = tuple([block_i,block_j])

                
                if board[i][j] == dot:
                    continue
                else:
                    if j not in j_dict:
                        j_dict[j] = []
                        j_dict[j].append(board[i][j])
                    else:
                        if board[i][j] in j_dict[j]:
                            return False
                        else:
                            j_dict[j].append(board[i][j])
                    
                    if i not in i_dict:
                        i_dict[i] = []
                        i_dict[i].append(board[i][j])
                    else:
                        if board[i][j] in i_dict[i]:
                            return False
                        else:
                            i_dict[i].append(board[i][j])

                    if block_num not in block_dict:
                        block_dict[block_num] = []
                        block_dict[block_num].append(board[i][j])
                    else:
                        if board[i][j] in  block_dict[block_num]:
                            return False
                        else:
                            block_dict[block_num].append(board[i][j])

                    
        return True