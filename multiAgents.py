
import random

class MultiAgentSearchAgent():

    def __init__(self, depth = '2'):
        """Initialize parameters for search

        Args:
            depth (str, optional): [How deep to search each branch]. Defaults to '2'.
        """
        self.index = 0
        self.depth = int(depth)


class ExpectimaxAgent(MultiAgentSearchAgent):

    def getAction(self, gameState):
        """[summary]

        Args:
            gameState ([state]): [tictactoe board state]

        Returns:
            [tuple]: [coordinate on board]
        """
        act = self.MM(gameState, 0, 0)
        return act


    def MM(self, gameState, depth, agentNum):
        """[Compute the optimal move using a MinMax Algorithm]

        Args:
            gameState ([state]): [tictactoe board state]
            depth ([int]): [how far down each branch to check]
            agentNum ([int]): [user move or computer move]

        Returns:
            [tuple]: [coordinate on board (game move)]
        """
        # change depth level after all agents have moved
        if agentNum >= 2:
            depth += 1
            agentNum = 0
        
        # check recursive base cases
        if depth == self.depth or gameState.evaluationFunction() in [10, -10, -5]:
            return gameState.evaluationFunction()
        
        actions = gameState.getLegalActions()
        optionalMoves = [self.MM(gameState.generateSuccessor(agentNum, act), depth, agentNum + 1) for act in actions]

        # Maximizing - pass all pacman moves
        if agentNum == 0:
            # Best/most-code-efficient way to return the best move
            if depth == 0:
                # Randomize selection
                maxOption = max(optionalMoves)
                topOptions = [i for i in range(len(optionalMoves)) if optionalMoves[i] == maxOption]
                return actions[random.choice(topOptions)]

            return max(optionalMoves)
        
        # Minimizing - pass ghost moves
        else:
            return sum(optionalMoves) / len(optionalMoves)
