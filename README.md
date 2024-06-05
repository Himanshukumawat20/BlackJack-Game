# BlackJack-Game
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           


# Blackjack Game in Python

Welcome to the Blackjack game project! This is a simple command-line implementation of the classic card game Blackjack, where you play against the computer acting as the dealer.


## Introduction

This project is a simple command-line implementation of the classic card game Blackjack. It allows you to play against the computer, which acts as the dealer. The game follows standard Blackjack rules, where the objective is to have a hand value closer to 21 than the dealer without exceeding 21.

## Features

- Unlimited deck size
- Realistic card values (Aces can be 1 or 11)
- Simple and intuitive command-line interface
- Clear instructions and game state updates
- Ability to play multiple rounds

## Setup

### Prerequisites

- Python 3.x
- Internet connection (to download dependencies)

## Usage

To start the game, run the following command in your terminal:

```bash
python main.py
```


## Game Rules

- The deck is unlimited in size, and there are no jokers.
- Jack, Queen, and King all count as 10.
- Aces can count as 11 or 1, depending on which is more beneficial for the hand.
- The player starts with two cards and can choose to draw more cards or pass.
- The dealer must draw cards until their hand value is 17 or higher.
- The player wins if their hand value is closer to 21 than the dealer's without exceeding 21.

## Code Structure

- `main.py`: Main script to run the game.
- `art.py`: Contains ASCII art for the game logo (imported as `logo`).

## Key Functions

### `play()`
The main function that runs the game loop. It initializes the game, deals cards, and handles user interactions.

### `pick_card()`
Draws a random card from the deck.

### `calculate_score(hand)`
Calculates the score of a given hand, accounting for the special rules of Aces being 1 or 11.



