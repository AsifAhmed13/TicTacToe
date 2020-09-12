"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x =0 
    o = 0
    for i in range(3):
        for j in range(3):
            if(board[i][j]=='X'):
                x+=1
            elif(board[i][j]=='O'):
                o+=1
    if(x==o):
        return 'X'
    return 'O'
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    l = []
    for i in range(3):
        for j in range(3):
            if(board[i][j] is None):
                l.append([i,j])
    return l
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    playerchance = player(board)
    newboard = []
    for i in range(3):
        newboard.append(board[i])
    i,j = action
    newboard[i][j] = playerchance
    return newboard
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if(board[0][0]==board[1][1]==board[2][2] and (board[0][0] is not None)):
        return board[0][0]
    elif(board[0][2]==board[1][1]==board[2][0] and (board[0][2] is not None)):
        return  board[0][2]
    else:
        for i in range(3):
            if(board[i][0]==board[i][1]==board[i][2] and (board[i][0] is not None)):
                return board[i][0]
            elif(board[0][i]==board[1][i]==board[2][i] and (board[0][i] is not None)):
                return board[0][i]
    return None
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    win = winner(board)
    if(win=='X' or win=='O'):
        return True
    for i in range(3):
        for j in range(3):
            if(board[i][j] is None):
                return False
    return True

    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if(win=='X'):
        return 1
    if(win=='O'):
        return -1
    return 0
    raise NotImplementedError

def min_player(board):
    if(terminal(board)==True):
        return utility(board)
    all_actions = actions(board)
    l = len(all_actions)
    v = float("inf")
    for i in range(l):
        tempboard = []
        for j in range(3):
            b =[]
            for k in range(3):
                b.append(board[j][k])
            tempboard.append(b)
        val= max_player(result(tempboard,all_actions[i]))
        if(val<v):
            v =  val
    return v


def max_player(board):
    if(terminal(board)==True):
        return utility(board)
    all_actions = actions(board)
    l = len(all_actions)
    v = float("-inf")
    for i in range(l):
        tempboard= []
        for j in range(3):
            b = []
            for k in range(3):
                b.append(board[j][k])
            tempboard.append(b)
        val= min_player(result(tempboard,all_actions[i]))
        if(val>v):
            v= val
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if(terminal(board)==True):
        return None
    playerchance = player(board)
    if(playerchance=='X'):
        all_actions = actions(board)
        l = len(all_actions)
        v = float("-inf")
        a = 0
        for i in range(l):
            tempboard= []
            for j in range(3):
                b = []
                for k in range(3):
                    b.append(board[j][k])
                tempboard.append(b)
            val= min_player(result(tempboard,all_actions[i]))
            if(val>v):
                v= val
                a = all_actions[i]
        return a
    else:
        all_actions = actions(board)
        l = len(all_actions)
        v = float("inf")
        a = 0
        for i in range(l):
            tempboard= []
            for j in range(3):
                b = []
                for k in range(3):
                    b.append(board[j][k])
                tempboard.append(b)
            val= max_player(result(tempboard,all_actions[i]))
            if(val<v):
                v= val
                a = all_actions[i]
        return a



    raise NotImplementedError
