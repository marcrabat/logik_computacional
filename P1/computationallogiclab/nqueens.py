import itertools
import numpy as np
import sys

cont = 0

def nqueens(n):
    '''
    This function uses the other functions implemented above and returns a CNF formula representing the n queens problem.
    '''
    board=(np.array(range(int(n)*int(n)))+1).reshape(int(n),int(n))
    
    #initializing solution in string format
    solution = ""
    
    #updating solution with rows clauses
    for i in range(1,n+1):
        for j in range(1,n+1):
            solution += str(((i-1)*n)+j) + " "
        solution += "0 \n"
    
    #updating solution with columns clauses, to these, we iterate the matrix inversely
    for j in range(1,n+1):
        for i in range(1,n+1):
            solution += str(((i-1)*n)+j) + " "
        solution += "0\n"

    #transposing matrix to compute columns clauses with writeCNF
    boardT = board.T

    #rows
    for i in range(0,n): 
        solution += writeCNF(board[i])
    #columns
    for i in range(0,n): #columnas
        solution += writeCNF(boardT[i])
    tmp = createDiagonals(boardT)
    tmp.sort(key=len,reverse=True)

    '''
    #prints used to debug
    print boardT
    print tmp
    '''

    #diagonals
    for diagonal in tmp:#createDiagonals(boardT):
        solution += writeCNF(diagonal)
    
    return solution
    
def createDiagonals(board):
    ''' This function returns the diagonal elements for the chessboard 
    Input: n

    Output:
    A list containing all the diagonal elements of the chess board. For the case where n= 4, this should be 
    '''
    
    diags = [board[::-1,:].diagonal(i) for i in range(-board.shape[0]+1,board.shape[1])]
    diags.extend(board.diagonal(i) for i in range(board.shape[1]-1,-board.shape[0],-1)) 
    return [s for s in diags if len(s) > 1]

def writeCNF(VariableList):
    global cont #global counter to count number of clauses
    n = len(VariableList)
    res = ""
    #iterating for each pair of positions for generating all combinations in a row, column or diagonal
    for i in range(0,n-1):
        for j in range(1,n-i):
            cont = cont + 1 #the counter is updated every time we generate a new clause
            res += "-"+str(VariableList[i]) + " -" + str(VariableList[i+j]) +" 0\n"
    return res                                                   


def main(n):
    global cont
    n = int(n)
    solution=nqueens(n)
    header = "p cnf " + str((n*n)) +" " + str(cont+2*n) + "\n" #generating the header
    formula = header + solution
    text_file = open("nqueens_sol.cnf", "w")
    text_file.write(formula)
    text_file.close()

if __name__ == '__main__':
    kwargs = {}
    if len(sys.argv) > 1:
        kwargs['n'] = sys.argv[1]
    main(**kwargs)
