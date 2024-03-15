from getpass import getpass as input
print('Rock, Scissor and Paper\n-----------------------')
print("**Rules**\nSelect your move:\n1. Press R if you want to choose Rock\n2. Similarly, press S for Scissor, and\n3. Press P for Paper\n4. Type exit in your move(turn) anytime you wish to finalise and exit the game.")

player_1 = input('Player 1, Kindly enter your Name: ')
player_2 = input('Player 2, Kindly enter your Name:')

print(f"Computer Mahashay! Let's facilitate the play of Rock Scissor and Paper with {player_1} and {player_2}\n")

score1 = 0
score2 = 0
while True:
  player1Move = input("Player 1: ")
  if player1Move == 'exit':
    print(f'So this is it. {player_1} had enough. Now, {player_1} wishes to end the game.\nComputer Mahashay {player_1} aur {player_2} ka Khata Bahi Nikaliye aur Parinaam Batayiye.\n---------------------\n**Result**')
    if score1 > score2:
      print(f'{player_1}: {score1}\n{player_2}: {score2}\n{player_1} won by {score1 - score2} points\nThank You')
      break
    if score2 > score1:
      print(f'{player_1}: {score1}\n{player_2}: {score2}\n{player_1} won by {score2 - score1} points\nThank You')
      break
    if score1 == score2:
      print(f"{player_1}: {score1}\n{player_2}: {score2}\nClearly, it's a draw.\nThank You")
      break
  player2Move = input("Player 2: \n")
  if player2Move == 'exit':
    print(f'So this is it. {player_2} had enough. Now, {player_2} wishes to end the game.\nComputer Mahashay {player_1} aur {player_2} ka Khata Bahi Nikaliye aur Parinaam Batayiye.\n--------------------------------\n**Result**')
    if score1 > score2:
      print(f'{player_1}: {score1}\n{player_2}: {score2}\n{player_1} won by {score1 - score2} points\nThank You')
      break
    if score2 > score1:
      print(f'{player_1}: {score1}\n{player_2}: {score2}\n{player_1} won by {score2 - score1} points\nThank You')
      break
    if score1 == score2:
      print(f"{player_1}: {score1}\n{player_2}: {score2}\nClearly, it's a draw.\nThank You")
      break
  
  if player1Move.lower()=="r":
    if player2Move.lower()=="r":
      print(f"It's a Draw!!\nYou both picked Rock. Such a coincidence\n{player_1}: {score1}\n{player_2}: {score2}")
    elif player2Move.lower()=="s":
      score2 += 1
      print(f"{player_1} smashed {player_2}'s Scissors into dust with their Rock!\n{player_1}: {score1}\n{player_2}: {score2}")
    elif player2Move.lower()=="p":
      score1 += 1
      print(f"{player_1}'s Rock is smothered by {player_2}'s Paper!\n{player_1}: {score1}\n{player_2}: {score2}")
    else:
      print(f"Invalid Move {player_2}!")
  elif player1Move.lower()=="p":
    if player2Move.lower()=="r":
      score1 += 1
      print(f"{player_2}'s Rock is smothered by {player_1}'s Paper!\n{player_1}: {score1}\n{player_2}: {score2}")
    elif player2Move.lower()=="s":
      score2 += 1
      print(f"Player1's Paper is cut into tiny pieces by Player2's Scissors!\n{player_1}: {score1}\n{player_2}: {score2}")
    elif player2Move.lower()=="p":
      print(f"Two bits of paper flap at each other. Dissapointing. Draw.\n{player_1}: {score1}\n{player_2}: {score2}")
    else:
      print(f"Invalid Move {player_2}!")
  elif player1Move.lower()=="s":
    if player2Move.lower()=="r":
      score2 += 1
      print(f"{player_2}'s Rock makes metal-dust out of {player_1}'s Scissors\n{player_1}: {score1}\n{player_2}: {score2}")
    elif player2Move.lower() == "s":
      print(f"Ka-Shing! Scissors bounce off each other like a dodgy sword fight! Draw.\n{player_1}: {score1}\n{player_2}: {score2}")
    elif player2Move.lower()=="p":
      score1 += 1
      print(f"{player_1}'s Scissors make confetti out of {player_2}'s paper!\n{player_1}: {score1}\n{player_2}: {score2}")
    else:
      print(f"Invalid Move {player_2}!")
  else:
    print(f"Invalid Move {player_1}!")
  print('_________________________________________')
