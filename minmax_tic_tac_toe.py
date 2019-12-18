'''
Project by: Felipe de Oliveira

You just need to access the terminal and deploy it using python. 
'''

import random

class TicTacToe:

    def __init__(self):
        """Initialize with empty board"""
        self.board = [" ", " ", " ", 
                      " ", " ", " ", 
                      " ", " ", " "]

    def show(self):
        """Format and print board"""
        print("""
          {} | {} | {}
         -----------
          {} | {} | {}
         -----------
          {} | {} | {}
        """.format(*self.board))

    def clearBoard(self):
        self.board = [" ", " ", " ", 
                      " ", " ", " ", 
                      " ", " ", " "]

    def whoWon(self):
        if self.checkWin() == "X":
            return "X"
        elif self.checkWin() == "O":
            return "O"
        elif self.gameOver() == True:
            return "Nobody"

    def availableMoves(self):
        """Return empty spaces on the board"""
        moves = []
        for i in range(0, len(self.board)):
            if self.board[i] == " ":
                moves.append(i)
        return moves

    def getMoves(self, player):
        """Get all moves made by a given player"""
        moves = []
        for i in range(0, len(self.board)):
            if self.board[i] == player:
                moves.append(i)
        return moves

    def makeUserMove(self, position, player):
        """Make a move on the board"""
        available_moves = self.availableMoves()
        if position in available_moves:
            self.board[position] = player
        else:
            return "You must pick a empty spot!!"

    def makeMove(self, position, player):
        """Make a move on the board"""
        self.board[position] = player

    def checkWin(self):
        """Return the player that wins the game"""
        combos = ([0, 1, 2], [3, 4, 5], [6, 7, 8],
                  [0, 3, 6], [1, 4, 7], [2, 5, 8],
                  [0, 4, 8], [2, 4, 6])

        for player in ("X", "O"):
            positions = self.getMoves(player)
            for combo in combos:
                win = True
                for pos in combo:
                    if pos not in positions:
                        win = False
                if win:
                    return player

    def gameOver(self):
        """Return True if X wins, O wins, or draw, else return False"""
        if self.checkWin() != None:
            return True
        for i in self.board:
            if i == " ":
                return False
        return True

    def minimax(self, node, depth, player):
        """
        Recursively analyze every possible game state and choose
        the best move location.
        node - the board
        depth - how far down the tree to look
        player - what player to analyze best move for (currently setup up ONLY for "O")
        """
        if depth == 0 or node.gameOver():
            if node.checkWin() == "X":
                return 0
            elif node.checkWin() == "O":
                return 100
            else:
                return 50

        if player == "O":
            bestValue = 0
            for move in node.availableMoves():
                node.makeMove(move, player)
                moveValue = self.minimax(node, depth-1, 'X')
                node.makeMove(move, " ")
                bestValue = max(bestValue, moveValue)
            return bestValue
        
        if player == "X":
            bestValue = 100
            for move in node.availableMoves():
                node.makeMove(move, player)
                moveValue = self.minimax(node, depth-1, 'O')
                node.makeMove(move, " ")
                bestValue = min(bestValue, moveValue)
            return bestValue

def get_best_move(board, depth):

    starting_value = 40
    board_choices = []

    #set the player as the computer
    player = 'O'

    #run through all the available moves in the board
    for move in board.availableMoves():
        board.makeMove(move, player)

        #call the minimax algorithm, passing the board and the adversary
        move_value = board.minimax(board, depth-1, 'X')

        #set the move done to empty (reset it)
        board.makeMove(move, " ")

        """
        if the value of the move is over the neutral value defined previously, 
        it means that the move might be between the best moves available. The computer will run this move.

        However, if the move's value is equal to the neutral value it will create a array of possible moves.
        """
        if move_value > starting_value:
            board_choices = [move]
            break
        elif move_value == starting_value:
            board_choices.append(move)

    """
    If there are choices with value equal or higher than the neutral value, it will pick one randomly.
    If not, the computer will get a random position between all the available position in the board.
    """
    if len(board_choices) > 0:
        return random.choice(board_choices)
    else:
        return random.choice(board.availableMoves())

def restartGame(self):
    correct_answer = False
    while correct_answer == False:
        restart_game = str(input("Do you want to restart the game? (y / n): "))
        if restart_game == 'y':
            self.clearBoard()
            return 'continue'
        elif restart_game == 'n':
            print ('Bye!')
            return 'break'
        else:
            print('Pick a answer between "n" and "y"!')

#Actual game
if __name__ == '__main__':
    tictactoe = TicTacToe()
    tictactoe.show()

    keep_playing = True
    #keep running the game until it game is over.
    while keep_playing == True:

        if tictactoe.gameOver() == True or len(tictactoe.availableMoves()) == 0:
            print("Game Over. " + tictactoe.whoWon() + " Wins")
            restart_game = restartGame(tictactoe)
            if restart_game == 'continue':
                tictactoe.show()
                continue
            else:
                break

        person_move = int(input("You are X: Choose number from 1-9: "))
        if person_move < 10:
            #get person move and subtract 1 (it starts in 0)
            #make the movement
            move_return = tictactoe.makeUserMove(person_move-1, "X")
            if move_return:
                print (move_return)
                continue

            #show the board with the movements
            tictactoe.show()

            #test if there is available moves to be made
            if len(tictactoe.availableMoves()) > 0:
            #optimus is the name of the machine (computer)
                print("Optimus is playing...")
                ai_move = get_best_move(tictactoe, -1)
                tictactoe.makeMove(ai_move, "O")
                tictactoe.show()
            
        else:
            print("Attention!! Pick a number from 1-9.")

    
