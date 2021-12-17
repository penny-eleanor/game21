#!/usr/bin/env python3
"""
NAME
    Game21 - Scripting Languages Final

DESCRIPTION
    A fun game similar to blackjack: each player bets 25 or 50 cents,
    drawing cards to get as close to 21 as possible without going over.
    The players play against a computer dealer.

VERSION
    1.0

DATE
    2021.12.10

AUTHOR
    Penelope Harding
"""


import game21 as game

LINE_LENGTH = 40


def play_game():
    """
    play_game()
    Main outer while loop to keep playing rounds

    :return: n/a
    """
    again = 'y'
    game.display_game_intro()
    players = game.get_players()
    while again == 'y':
        game.play_round(players)
        game.display_round_summary(players)
        print(LINE_LENGTH * '=')
        again = game.get_yn_input(prompt="\tDo you want to play again? (y/n): ")
        print(LINE_LENGTH * '=')
    input('later skater. press any key to continue')


if __name__ == "__main__":
    play_game()
