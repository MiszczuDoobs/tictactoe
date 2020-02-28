def check_winner(current_player):
  #horizontal
  if board[0] and board[1] and board[2] == current_player:
    win(current_player)
  elif board[3] and board[4] and board[5] == current_player:
    win(current_player)
  elif board[6] and board[7] and board[8] == current_player:
    win(current_player)
  
  #vertical
  elif board[0] and board[3] and board[6] == current_player:
    win(current_player)
  elif board[1] and board[4] and board[7] == current_player:
    win(current_player)
  elif board[2] and board[5] and board[8] == current_player:
    win(current_player)

  #diagonal
  elif board[0] and board[4] and board[8] == current_player:
    win(current_player)

  elif board[2] and board[4] and board[6] == current_player:
    win(current_player)