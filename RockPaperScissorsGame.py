#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 10:36:58 2018

@author: newarbhai
"""
print("ROCK")
print("PAPER")
print("Scissors")

player1 = input("Player 1, Make your move: ")
player2 = input("Player 2, make your move: ")

if player1 == "rock" and player2=="scissors":
    print("player 1 wins")
elif player1=="rock" and player2=="paper":
    print("player 2 wins")
elif player1=="paper" and player2=="rock":
    print("player 1 wins")
elif player1=="scissors" and player2=="rock":
    print("player 2 wins")
elif player1=="scissors" and player2=="paper":
    print("player 1 wins")
elif player1==player2:
    print("Its a tie !!" + "Do again")
else:
    print("Something went wrong, type correct !!")
    


