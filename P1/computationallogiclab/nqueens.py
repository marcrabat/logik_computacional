import itertools
import numpy as np
import sys

def nqueens(n, ready=False):
    '''
    This function uses the other functions implemented above and returns a CNF formula representing the n queens problem.
    '''
    board=(np.array(range(int(n)*int(n)))+1).reshape(int(n),int(n))
    a = createDiagonals(board)
    print a
    print board
    for i in range(0,len(board)):
        print board[i,:]

    
    if ready:
        return conditions

    




def createDiagonals(board):
    ''' This function returns the diagonal elements for the chessboard 

    Input: n

    Output:
    A list containing all the diagonal elements of the chess board. For the case where n= 4, this should be 
    


    '''
    
    diags = [board[::-1,:].diagonal(i) for i in range(-board.shape[0]+1,board.shape[1])]
    diags.extend(board.diagonal(i) for i in range(board.shape[1]-1,-board.shape[0],-1)) 
    return [s for s in diags if len(s) > 1]




def AtLeastOne(VariableList):
    ''' This function models the uniqueness condition over the input list. 
    ie, for a list of inputs [X1, X2, X3, X4...] Only one of the inputs can be true

    Input: List of strings

    Output:
    String of formula modeling the uniqueness condition, output with () around the formula


    '''





def AtMostOne(VariableList):

    ''' This function models the at most one condition over the input list. 
    ie, for a list of inputs [X1, X2, X3, X4...] At most one of the inputs can be true

    Input: List of strings

    Output:
    String of formula modeling the condition, output with () around the formula


    '''




def main(n):
    ready=False
    solution=nqueens(n,ready)
    if ready:
        text_file = open("nqueens_sol.cnf", "w")
        text_file.write(solution)
        text_file.close()

if __name__ == '__main__':
    kwargs = {}
    if len(sys.argv) > 1:
        kwargs['n'] = sys.argv[1]
    main(**kwargs)
