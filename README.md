# Blackjack Game with Python

A blackjack game created in Python which try to simulate a real one.

This is a Text-based Blackjack game.The game is based on the description provided in the [wikipedia](https://en.wikipedia.org/wiki/Blackjack).The objective of the game is to beat the dealer, which can be done in the following ways:

  - Get 21 points on the player's first two cards (called a blackjack), without the dealer having blackjack;
  - Reach a final score higher than the dealer without exceeding 21; 
  - Let the dealer draw additional cards until his or her hand exceeds 21.

The game is implemented with standard 1 deck of cards.It has implementation of two standard options for player after receiving two initial cards: Hit and Stand.The rules for each implementation is described below:
  - __Hit__: Take another card from dealer.
  - __Stand__:Player takes no more cards and dealer draws the card.

Following rules are implemented for the dealer in the game:
  - Dealer hits until his cards total 17 or more points.
 
Following rules are implemented for different scenario of the game:
  - A blackjack beats any hand that is not a blackjack, even one with a value of 21.
  - An outcome of blackjack vs. blackjack results in a tie.
  - The winner is declared after the dealer has finished taking cards from the deck and comparing the player's hand to the dealer's hand.

# Sample output of program
### Sample output 1:
```
How many games do you want to play? 3

******************************
Game 1 of 3
******************************
Your hand: 
┌───────┐
|4      |
|       |
|   ♦   |
|       |
|     4 |
└───────┘
┌───────┐
|5      |
|       |
|   ♠   |
|       |
|     5 |
└───────┘

Dealer's hand: 
┌───────┐
|   h   |
|   i   |
|   d   |
|   d   |
|   e   |
|   n   |
└───────┘
┌───────┐
|8      |
|       |
|   ♥   |
|       |
|     8 |
└───────┘

Please choose 'Hit' or 'Stand' (or h/s) : h

Your hand: 
┌───────┐
|4      |
|       |
|   ♦   |
|       |
|     4 |
└───────┘
┌───────┐
|5      |
|       |
|   ♠   |
|       |
|     5 |
└───────┘
┌───────┐
|K      |
|       |
|   ♣   |
|       |
|     K |
└───────┘

Please choose 'Hit' or 'Stand' (or h/s) : s

Dealer's hand: 
┌───────┐
|3      |
|       |
|   ♦   |
|       |
|     3 |
└───────┘
┌───────┐
|8      |
|       |
|   ♥   |
|       |
|     8 |
└───────┘
┌───────┐
|A      |
|       |
|   ♦   |
|       |
|     A |
└───────┘
┌───────┐
|8      |
|       |
|   ♦   |
|       |
|     8 |
└───────┘

Final Results: 
Your hand:  19
Dealer's hand:  20
Dealer wins! 😭

******************************
Game 2 of 3
******************************
Your hand: 
┌───────┐
|9      |
|       |
|   ♣   |
|       |
|     9 |
└───────┘
┌───────┐
|A      |
|       |
|   ♠   |
|       |
|     A |
└───────┘

Dealer's hand: 
┌───────┐
|   h   |
|   i   |
|   d   |
|   d   |
|   e   |
|   n   |
└───────┘
┌───────┐
|8      |
|       |
|   ♠   |
|       |
|     8 |
└───────┘

Please choose 'Hit' or 'Stand' (or h/s) : s

Dealer's hand: 
┌───────┐
|2      |
|       |
|   ♣   |
|       |
|     2 |
└───────┘
┌───────┐
|8      |
|       |
|   ♠   |
|       |
|     8 |
└───────┘
┌───────┐
|4      |
|       |
|   ♥   |
|       |
|     4 |
└───────┘
┌───────┐
|6      |
|       |
|   ♣   |
|       |
|     6 |
└───────┘

Final Results: 
Your hand:  20
Dealer's hand:  20
Tie! 😑

******************************
Game 3 of 3
******************************
Your hand: 
┌───────┐
|3      |
|       |
|   ♦   |
|       |
|     3 |
└───────┘
┌───────┐
|K      |
|       |
|   ♥   |
|       |
|     K |
└───────┘

Dealer's hand: 
┌───────┐
|   h   |
|   i   |
|   d   |
|   d   |
|   e   |
|   n   |
└───────┘
┌───────┐
|2      |
|       |
|   ♠   |
|       |
|     2 |
└───────┘

Please choose 'Hit' or 'Stand' (or h/s) : h

Your hand: 
┌───────┐
|3      |
|       |
|   ♦   |
|       |
|     3 |
└───────┘
┌───────┐
|K      |
|       |
|   ♥   |
|       |
|     K |
└───────┘
┌───────┐
|7      |
|       |
|   ♥   |
|       |
|     7 |
└───────┘

Please choose 'Hit' or 'Stand' (or h/s) : s

Dealer's hand: 
┌───────┐
|6      |
|       |
|   ♠   |
|       |
|     6 |
└───────┘
┌───────┐
|2      |
|       |
|   ♠   |
|       |
|     2 |
└───────┘
┌───────┐
|Q      |
|       |
|   ♠   |
|       |
|     Q |
└───────┘

Final Results: 
Your hand:  20
Dealer's hand:  18
You win! 🤩

 Thanks for playing!
 
 ```


### Sample output 2(Tie Case):
```
How many games do you want to play? 1
******************************
Game 1 of 1
******************************
Your hand: 
┌───────┐
|10     |
|       |
|   ♠   |
|       |
|     10|
└───────┘
┌───────┐
|9      |
|       |
|   ♥   |
|       |
|     9 |
└───────┘

Dealer's hand: 
┌───────┐
|   h   |
|   i   |
|   d   |
|   d   |
|   e   |
|   n   |
└───────┘
┌───────┐
|6      |
|       |
|   ♦   |
|       |
|     6 |
└───────┘

Please choose 'Hit' or 'Stand' (or h/s) : s

Dealer's hand: 
┌───────┐
|5      |
|       |
|   ♠   |
|       |
|     5 |
└───────┘
┌───────┐
|6      |
|       |
|   ♦   |
|       |
|     6 |
└───────┘
┌───────┐
|8      |
|       |
|   ♠   |
|       |
|     8 |
└───────┘

Final Results: 
Your hand:  19
Dealer's hand:  19
Tie! 😑

 Thanks for playing!

```
### Sample output 3(BlackJack Case):
```

How many games do you want to play? 1

******************************
Game 1 of 1
******************************
Your hand: 
┌───────┐
|A      |
|       |
|   ♦   |
|       |
|     A |
└───────┘
┌───────┐
|K      |
|       |
|   ♥   |
|       |
|     K |
└───────┘

Dealer's hand: 
┌───────┐
|   h   |
|   i   |
|   d   |
|   d   |
|   e   |
|   n   |
└───────┘
┌───────┐
|10     |
|       |
|   ♥   |
|       |
|     10|
└───────┘

You have blackjack. You win! 🤩

 Thanks for playing!
 
 ```
