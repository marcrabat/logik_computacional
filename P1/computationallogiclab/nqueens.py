import itertools
import numpy as np
import sys


def nqueens(n):
    '''
    This function uses the other functions implemented above and returns a CNF formula representing the n queens problem.
    '''
    board=(np.array(range(int(n)*int(n)))+1).reshape(int(n),int(n))
    boardT = board.T
    solution = " "
    for i in range(0,n): #lineas
        solution += writeCNF(board[i])
    for i in range(0,n): #columnas
        solution += writeCNF(boardT[i])
    for diagonal in createDiagonals(board):
        solution += writeCNF(diagonal)
    return solution

"""
def nQueenProblem( n ):
  queens = [0]*n
  addQueen( 0, queens, n )
  return queens
 
def addQueen( x, queens, n ):
  i = 0
  while i < n and 0 == queens[n - 1]:
    if safeToAdd( x, i, queens ):
      queens[x] = [x,i]
      addQueen( x + 1, queens, n )
    i += 1
 
def safeToAdd( x, y, queens ):
  for i in range( x ):
    if y == queens[i][1] or ( x - y ) == ( i - queens[i][1] ) or ( x + y )== ( i + queens[i][1] ):
      return False
  return True"""
    

    
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
    '''

    '''
    n = len(VariableList)
    res = " "
    for i in range(0,n-1):
        for j in range(1,n-i):
            res += "-"+str(VariableList[i]) + "-" + str(VariableList[i+j]) +" 0\n"
    return res                                                   

def AtMostOne(VariableList):

    ''' This function models the at most one condition over the input list. 
    ie, for a list of inputs [X1, X2, X3, X4...] At most one of the inputs can be true

    Input: List of strings

    Output:
    String of formula modeling the condition, output with () around the formula


    '''




def main(n):
    global cont
    n = int(n)
    solution=nqueens(n)
    text_file = open("nqueens_sol.cnf", "w")
    text_file.write(solution)
    text_file.close()

if __name__ == '__main__':
    kwargs = {}
    if len(sys.argv) > 1:
        kwargs['n'] = sys.argv[1]
    main(**kwargs)
