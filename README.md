# Blackjack Game with Python

A blackjack game created in Python which try to simulate a real one.

This is a Text-based Blackjack game.The game is based on the description provided in the [wikipedia](https://en.wikipedia.org/wiki/Blackjack).The objective of the game is to beat the dealer, which can be done in the following ways:

  - Get 21 points on the player's first two cards (called a blackjack), without the dealer having blackjack;
  - Reach a final score higher than the dealer without exceeding 21; 
  - Let the dealer draw additional cards until his or her hand exceeds 21.

The game is implemented with standard 1 deck of cards.It has implementation of two standard options for player after receiving two initial cards: Hit and Stand.The rules for each implementation is described below:
  - Hit: Take another card from dealer.
  - Stand:Player takes no more cards and dealer draws the card.

Following rules are implemented for the dealer in the game:
  - Dealer hits until his cards total 17 or more points.
 
Following rules are implemented for different scenario of the game:
  - A blackjack beats any hand that is not a blackjack, even one with a value of 21.
  - An outcome of blackjack vs. blackjack results in a tie.
  - The winner is declared after the dealer has finished taking cards from the deck and comparing the player's hand to the dealer's hand.

# Sample output of program
Sample output 1:
