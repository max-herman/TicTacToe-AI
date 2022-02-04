
from copy import deepcopy

class gameState():
    def __init__(self, pos=[[2,2,2], [2,2,2], [2,2,2]]):
        self.game = pos
        self.rep = {0: 'x', 1: 'o', 2: ' '}


    def draw(self):
        """[check whether the game is in a drawn state]

        Returns:
            [bool]: [true if drawn]
        """
        flat = []
        for i in range(len(self.game)):
            flat.extend(self.game[i])

        if 2 not in flat:
            return True


    def getLegalActions(self):
        """[generate a list of possible moves]

        Returns:
            [list]: [all legal moves]
        """
        legalPos = []
        for i in range(len(self.game)):
            for j in range(len(self.game[0])):
                if self.game[i][j] == 2:
                    legalPos.append([i, j])

        return legalPos
    

    def printBoard(self):
        """[display game board in ASCII]
        """
        board = deepcopy(self.game)
        for i in range(len(self.game)):
            for j in range(len(self.game[0])):
                board[i][j] = self.rep[self.game[i][j]]

        for i in range(len(board)):
            print(board[i])

    
    def generateSuccessor(self, agentNum, act):
        """[Copy the state for the MinMax recursive functionality]

        Args:
            agentNum ([int]): [user or computer]
            act ([tuple]): [action / move]

        Returns:
            [gameState]: [new gameState object]
        """
        
        currentGame = deepcopy(self.game)
        currentGame[act[0]][act[1]] = agentNum
        return gameState(currentGame)
    

    def evaluationFunction(self):
        """[Generate score of current state]

        Returns:
            [type]: [description]
        """

        pos = self.game
        checks = [check_col(pos), check_row(pos), check_diag(pos)]

        # Good score if computer is winning, bad score if user is winning or drawn game
        if self.draw():
            return -5
        elif 1 not in checks and 0 not in checks:
            return 0
        elif 0 in checks:
            return 10
        elif 1 in checks:
            return -10


def check_col(currentGameState):
    """[Collect all previous moves on board at each collumn]

    Args:
        currentGameState ([gameState]): [game board]

    Returns:
        [int]: [1, 0, or -1]
    """

    for j in range(len(currentGameState[0])):
        p = currentGameState[0][j]

        if p != 2:

            win = 0
            for i in range(len(currentGameState)):
                if currentGameState[i][j] != p:
                    win = 1
                    break
            
            if win == 0:
                return p
    
    return -1


def check_row(currentGameState):
    """[Collect all previous moves on board at each row]

    Args:
        currentGameState ([gameState]): [game board]

    Returns:
        [int]: [1, 0, or -1]
    """

    for i in range(len(currentGameState)):
        p = currentGameState[i][0]

        if p != 2:

            win = 0
            for j in range(len(currentGameState[0])):
                if currentGameState[i][j] != p:
                    win = 1
                    break
            
            if win == 0:
                return p
    
    return -1


def check_diag(currentGameState):
    """[Collect all previous moves on board along the two diagonals]

    Args:
        currentGameState ([gameState]): [game board]

    Returns:
        [int]: [1, 0, or -1]
    """

    i_r = len(currentGameState)
    j_r = len(currentGameState[0])

    # forward diagonal
    p = currentGameState[0][0]

    if p != 2:
        win = 0
        i = 0
        j = 0

        while i < i_r and j < j_r:

            if currentGameState[i][j] != p:
                win = 1
                break
            
            i += 1
            j += 1
            
        if win == 0:
            return p
    
    # backward diagonal
    p = currentGameState[i_r - 1][0]
    if p != 2:
        win = 0
        i = i_r - 1
        j = 0

        while i >= 0 and j < j_r:

            if currentGameState[i][j] != p:
                win = 1
                break

            i -= 1
            j += 1
            
        if win == 0:
            return p
    
    return -1
