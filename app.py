class Game:
  def __init__(self, turn, tie, winner, board):
    self.turn = turn
    self.tie = tie
    self.winner = winner
    self.board = board
    
  def play_game(self):
    print("Hello, Welcome to Tic-Tac-Toe Game")
  
  def print_board(self):
    b = self.board
    print(f"""{b['a1'] or ' '}
        A   B   C
    1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
        ----------
    2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
        ----------
    3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
  """)

  def print_message(self):
    ## If there is a tie: print("Tie game!")
    ## If there is a winner: print(f"{self.winner} wins the game!")
    ## Otherwise: print(f"It's player {self.turn}'s turn!")
    print(f'{self.turn} turn')

  def render(self):
    # Call upon print_board
    self.print_board()
    ## Call upon print_message
    self.print_message()
    
  def get_move(self):
    while True:
      # prompt user for input
      move = input(f"Enter a valid movie (example: A1): ").lower()
      
      # If the input is valid, update the board and break the loop
      if move == 'a1' or move == 'a2' or move == 'a3' or move == 'b1' or move == 'b2' or move == 'b3' or move == 'c1' or move == 'c2' or move == 'c3':
        print(move)
        print(self.board[move])
        if self.board[move] == None:
          self.board[move] = self.turn
          break
        else: 
          # otherwise, print a message notifying the user of the invalid input and allow the loop to continue
          print("This cell is already occupied, select another cell.")
      else:
        print("invalid input")

game_instance = Game("X", False, None, {
  'a1': None, 'b1': None, 'c1': None,
  'a2': None, 'b2': None, 'c2': None,
  'a3': None, 'b3': None, 'c3': None,
} )

game_instance.play_game()
game_instance.render()
game_instance.get_move()