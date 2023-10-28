import random

class TTT_cs170_judge:
    def __init__(self):
        self.board = []

    def create_board(self, n):
        for i in range(n):
            row = []
            for j in range(n):
                row.append('-')
            self.board.append(row)

    def display_board(self):
        for row in self.board:
            print(" ".join(row))
        print()

    def is_winner(self, player):
        # Check rows
        for row in self.board:
            if all([cell == player for cell in row]):
                return True

        # Check columns
        for col in range(len(self.board)):
            if all([self.board[row][col] == player for row in range(len(self.board))]):
                return True

        # Check diagonals
        if all([self.board[i][i] == player for i in range(len(self.board))]):
            return True
        if all([self.board[i][len(self.board) - i - 1] == player for i in range(len(self.board))]):
            return True

        return False

    def is_board_full(self):
        return all([cell in ['X', 'O'] for row in self.board for cell in row])

class Player_1:
    def __init__(self, judge):
        self.board = judge.board

    def my_play(self):
        while True:
            row, col = map(int, input("Enter the row and column numbers separated by space: ").split())

            if 1 <= row <= len(self.board) and 1 <= col <= len(self.board[0]):
                if self.board[row-1][col-1] == '-':
                    self.board[row-1][col-1] = 'X'
                    break
                else:
                    print("Invalid move. Cell already occupied!")
            else:
                print("Invalid move. Out of bounds!")

class Player_2:
    def __init__(self, judge):
        self.judge = judge
        self.board = judge.board

    def my_play(self):
        if self.judge.is_winner('O') or self.judge.is_winner('X'):
            return

        bestMove = self.aiMove(self.board)

        if bestMove:
            i, j = bestMove
            self.board[i][j] = 'O'
        #else:
        #    print("It's a tie!")

    def aiMove(self, board):

        alpha = float('-inf')
        beta = float('inf')
        highScore = float('-inf')
        bestMove = None

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '-':
                    board[i][j] = 'O'
                    score = self.minimax(board, 0, False, alpha, beta)
                    board[i][j] = '-'

                    if highScore < score:
                        bestMove = (i, j)
                        highScore = score
                    
                    alpha = max(alpha, highScore)

                    if alpha >= beta:
                        break

        return bestMove

    def minimax(self, board, depth, is_maximizing, alpha, beta):

        if self.judge.is_winner('O'):
            return 1
        
        if self.judge.is_board_full():
            return 0
        
        if self.judge.is_winner('X'):
            return -1

        if is_maximizing:
            highScore = float('-inf')

            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == '-':
                        board[i][j] = 'O'
                        score = self.minimax(board, depth + 1, False, alpha, beta)
                        #score = self.minimax(board, depth, True, alpha, beta)
                        board[i][j] = '-'
                        highScore = max(score, highScore)
                        alpha = max(alpha, highScore)

                        if beta <= alpha:
                            break

            return highScore
        
        else:
            highScore = float('inf')

            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == '-':
                        board[i][j] = 'X'
                        score = self.minimax(board, depth + 1, True, alpha, beta)
                        #score = self.minimax(board, depth, True, alpha, beta)
                        board[i][j] = '-'
                        highScore = min(score, highScore)
                        beta = min(beta, highScore)

                        if beta <= alpha:
                            break

            return highScore


def game_loop():
    n = 3  # Board size
    game = TTT_cs170_judge()
    game.create_board(n)
    player1 = Player_1(game)
    player2 = Player_2(game)
    starter = random.randint(0, 1)
    win = False
    if starter == 0:
        print("Player 1 starts.")
        game.display_board()
        while not win:
            player1.my_play()
            win = game.is_winner('X')
            game.display_board()
            if win:
                print("Player 1 wins!")
                break
            if game.is_board_full():
                print("It's a tie!")
                break

            player2.my_play()
            win = game.is_winner('O')
            game.display_board()
            if win:
                print("Player 2 wins!")
                break
            if game.is_board_full():
                print("It's a tie!")
                break
    else:
        print("Player 2 starts.")
        game.display_board()
        while not win:
            player2.my_play()
            win = game.is_winner('O')
            game.display_board()
            if win:
                print("Player 2 wins!")
                break
            if game.is_board_full():
                print("It's a tie!")
                break

#game_loop() # Uncomment this line to play the game, but it must be commented again when you are submitting the code
