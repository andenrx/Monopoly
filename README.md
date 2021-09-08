# Monopoly
----------
# For Interactive Version try it on [Google Colab](https://colab.research.google.com/drive/1HkM5sumCGutjZLHW3eh8ynR4g7aaUW7x?usp=sharing)

This project analyzes the movement behind the game of Monopoly. Specifically, we can model the movement as a *Markov Chain* since the probability of landing on a tile depends only on position of the player at the start of the turn. The derivation uses quite a bit of Linear Algebra to find the probability of a player ending up on a given tile after $n$ turns as well as the limiting distribution as $n \to \infty$.  Additionally, the project takes a look at the average number of turns to travel from one space to another.

All code is in Python using Numpy for the Linear Algebra.
