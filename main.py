############### Blackjack Project #####################
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/

from art import logo
import random
from replit import clear

def play():
  print(logo)
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  def pick_card():
    return random.choice(cards)
  user_card = []
  computer_card = []
  user_score = 0
  computer_score = 0
  user_card.append(pick_card())
  user_card.append(pick_card())
  user_score = sum(user_card)
  computer_card.append(pick_card())
  computer_card.append(pick_card())
  print(f"    Your cards: {user_card}, current score: {user_score}")
  print(f"    Computer's first card: {computer_card[0]}")

  if 11 in user_card and len(user_card) == 2:
    user_score -= 10  
    for i in range(len(user_card)):
      if user_card[i] == 11:
        user_card[i] = 1
  if 11 in computer_card and len(computer_card) == 2:
    computer_score -= 10
  new_card = input("Type 'y' to get another card, type 'n' to pass: ")
  
  if new_card == 'y':
    user_card.append(pick_card())
    user_score = sum(user_card)
    computer_score = sum(computer_card)
    print(f"    Your final hand: {user_card}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_card}, final score: {computer_score}")
  elif new_card == 'n':
   
    if user_score < 17:
      print("Your score is less than 17, You need to get more cards")
      new_card = input("Get another card? Type 'y' or 'n': ")
      if new_card == 'y':
        user_card.append(pick_card())
      elif new_card == 'n':
          print("Your score is less than 17, You need to get more cards")

    if computer_score < 17:
      computer_card.append(pick_card())
      computer_score = sum(computer_card)
    print(f"    Your final hand: {user_card}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_card}, final score: {computer_score}")
  if user_score > 21:
    print("You wentover, You lose \U0001F622") 

  elif computer_score > 21:
    print("Opponent went over, You win \U0001F604")
    

  elif user_score > computer_score:
    print("You win \U0001F604")
    

  elif user_score == computer_score:
    print("Draw \U0001F624")
    
  elif computer_score > user_score:
    print("You Lose \U0001F622")
    

  start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

  if start == 'y':
    play()  
  else:
    clear()
  

running = True
start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

if start == 'y':
  play()  
else:
  clear()



