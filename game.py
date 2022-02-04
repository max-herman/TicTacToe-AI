
import multiAgents
import state
import sys

if __name__ == "__main__":

    user = int(sys.argv[1])
    n = int(sys.argv[2])
    d = int(sys.argv[3])
    g = state.gameState(pos=[[2 for i in range(n)] for j in range(n)])

    agent = multiAgents.ExpectimaxAgent(depth=d)
    turn = 0

    if user == 0:
        turn = 1
    
    # play moves until game ends (win or draw)
    while g.evaluationFunction() == 0:

        # run MinMax algorithm to find optimal move
        if turn == 0:
            print("Computer:")
            act = agent.getAction(g)
        
        # query user for move
        if turn == 1:
            print("Player:")
            i,j = input("Move (i,j):").split(",")

            while [int(j), int(i)] not in g.getLegalActions():
                i,j = input("Make a legal move please (i,j):").split(",")

            act = [int(j), int(i)]

        g = g.generateSuccessor(turn, act)

        g.printBoard()

        if turn == 0:
            turn = 1
        else:
            turn = 0
    
    print(g.evaluationFunction())
