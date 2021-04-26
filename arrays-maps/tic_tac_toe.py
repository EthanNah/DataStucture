# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 3: DID I WIN TIC-TAC-TOE?
#
# NAME:         FIXME
# ASSIGNMENT:   Technical HW: Arrays & Maps

# takes a player character and a 2-dimensional
# array as parameters and returns whether the
# player won the game
# HINT: What does a boolean accumulator look like?
def did_I_win_2D(player, board):

  nrow=len(board)
  ncols=len(board[0])
  counter=0
  counter_re=0
  counter_row=0
  counter_col=0

  cond=False
 
  for i in range(nrow):

     #dignal(왼쪽 대각선)
    if (board[i][i] == player):
          counter += 1 
    #reverse dignal
    if(board[i][nrow-i-1]==player):
        counter_re += 1 

    for j in range(ncols): 
      #row
      if board[i][j] ==player:
        counter_row += 1

    if (counter_row!=0) and (counter_row%ncols)==0:
       
      cond=True
      break
    else:
      counter_row=0  
  
  for i in range(ncols):  
    for j in range(nrow): 
      #col
      if board[j][i] ==player:
        counter_col += 1 

     
    if (counter_col!=0) and (counter_col%ncols==0):
   
      cond=True
      break
    else:
      counter_col=0  
   
  if (counter!=0 and counter%nrow==0) or (counter_re!=0  and counter_re%nrow==0):
     
    cond=True     

  return cond

def print_2D_board(b):
    for i in range(len(b)):
        print(b[i])

def main():
    boards = [ [["X", "O", "O"]] * 3, \
               [["X", "O", "X"], ["O"] * 3, ["O", "X", "O"]], \
               [['O', 'O', 'X'], ['O', 'X', 'O'], ['X', 'O', 'O']], \
               [["O", "O", "X"]] * 3 ]
    #did_I_win_2D("X",boards)
    for b in boards:
      print_2D_board(b)
      print("-----------------")
      print("O won?", did_I_win_2D("O", b))
      print("-----------------")
      print("X won?", did_I_win_2D("X", b))
      print("-----------------")
      

# Don't run main on import
if __name__ == "__main__":
    main()