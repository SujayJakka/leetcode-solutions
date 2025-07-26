class Solution(object):
    def isValidSudoku(self, board):
        #rows
        for i in range(0, 9):
            newthing = []
            for j in range(0,9):
                s1 = board[i][j]
                if(s1 == "."):
                    continue
                newthing.append(s1)
            if(len(set(newthing)) != len(newthing)):
                    return False
        #columns
        for x in range(0, 9):
            newthing = []
            for y in range(0, 9):
                s1 = board[y][x]
                if(s1 == "."):
                    continue
                newthing.append(s1)
            if(len(set(newthing)) != len(newthing)):
                return False
            
        #3x3 check 1
        newlist1 = []
        for q in range(0,3):
            for w in range(0,3):
                if(board[q][w] != "."):
                    newlist1.append(board[q][w])
        if(len(set(newlist1)) != len(newlist1)):
            return False
        
        #3x3 check 2
        newlist2 = []
        for q in range(0,3):
            for w in range(3,6):
                if(board[q][w] != "."):
                    newlist2.append(board[q][w])
        if(len(set(newlist2)) != len(newlist2)):
            return False
        
        #3x3 check 3
        newlist3 = []
        for q in range(0,3):
            for w in range(6,9):
                if(board[q][w] != "."):
                    newlist3.append(board[q][w])
        if(len(set(newlist3)) != len(newlist3)):
            return False
        
        #3x3 check 4
        newlist4 = []
        for q in range(3,6):
            for w in range(0,3):
                if(board[q][w] != "."):
                    newlist4.append(board[q][w])
        if(len(set(newlist4)) != len(newlist4)):
            return False
        
        #3x3 check 5
        newlist5 = []
        for q in range(3,6):
            for w in range(3,6):
                if(board[q][w] != "."):
                    newlist5.append(board[q][w])
        if(len(set(newlist5)) != len(newlist5)):
            return False
        
        #3x3 check 6
        newlist6 = []
        for q in range(3,6):
            for w in range(6,9):
                if(board[q][w] != "."):
                    newlist6.append(board[q][w])
        if(len(set(newlist6)) != len(newlist6)):
            return False
        
        #3x3 check 7
        newlist7 = []
        for q in range(6,9):
            for w in range(0,3):
                if(board[q][w] != "."):
                    newlist7.append(board[q][w])
        if(len(set(newlist7)) != len(newlist7)):
            return False
        
        #3x3 check 8
        newlist8 = []
        for q in range(6,9):
            for w in range(3,6):
                if(board[q][w] != "."):
                    newlist8.append(board[q][w])
        if(len(set(newlist8)) != len(newlist8)):
            return False
        
        #3x3 check 9
        newlist9 = []
        for q in range(6,9):
            for w in range(6,9):
                if(board[q][w] != "."):
                    newlist9.append(board[q][w])
        if(len(set(newlist9)) != len(newlist9)):
            return False
        
        return True
        
        