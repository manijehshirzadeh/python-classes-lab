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

game_instance = Game("X", False, None, {
  'a1': None, 'b1': None, 'c1': None,
  'a2': None, 'b2': None, 'c2': None,
  'a3': None, 'b3': None, 'c3': None,
} )

game_instance.play_game()
game_instance.print_board()