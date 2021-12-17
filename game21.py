#!/usr/bin/env python3

def get_yn_input(prompt):
    """
    get_yn_input(prompt)
    Displays a yes/no prompt and returns with either y or n

    :param prompt:
    :return: the user's response (y/n)
    """


def display_game_intro():
    """
    display_game_intro()
    Displays the game title and the rules of the game

    :return: n/a
    """


def get_players():
    """
    get_players()
    Gets the players names, adding them to the dictionary and setting initial data
    Stops when user enters the word 'done'
        set cash to $1.0
        set cards to an empty list
        set cards_total to 0
        set bet to 0.25 default value

    :return: n/a
    """


def play_round(players):
    """
    Call each function required to play one round
        1. setup the new round
        2. deal to each player
        3. deal to the dealer
        4. display the winners

    :param players: 2D dictionary of all players' data
    :return: n/a
    """


def setup_new_round(players):
    """
    setup_new_round(players)
    Reset all player's data for the next round.
        set cash to $1.0
        set cards to an empty list
        set cards_total to 0
        set bet to 0.25 default value

    :param players: 2D dictionary of all players' data
    :return: n/a
    """


def deal_card(player_info):
    """
    deal_card(player_info)
    Does the following three items:
        Generate a random number between 1-10
        add it to the card to the list of cards
        add the card value to the cards total

    :param player_info: 2D dictionary of all players' data
    :return: n/a
    """


def deal_to_players(players):
    """
    deal_to_players(players)
    Deal to all players using a for loop through the 2D dictionary
        if the player is out of money then continue
        else automatically deal them two cards
        and then ask the player if they want another cards as long as they don't exceed 21
        if they exceed 21 then continue to the next player
        else ask them if they want to double their bet as long as they have at least 50 cents

    :param players: 2D dictionary of all players' data
    :return: n/a
    """


def deal_to_dealer(players):
    """
    deal_to_dealer(players)
    If there are no players still playing this hand (they did not exceed 21)
    then the dealer automatically wins
    Otherwise start dealing to the dealer until he beats all players or reaches 21

    :param players: 2D dictionary of all players' data
    :return: n/a
    """


def display_cards(cards):
    """
    display_cards(cards)
    Display one player's current list of cards on one line

    :param cards: one player's current cards
    :return: n/a
    """


def display_winners(players, dealer_cards_total):
    """
    display_winners(players, dealer_cards_total)
    Display the winners for the current round

    :param players: 2D dictionary of all players' data
    :param dealer_cards_total: the dealer's card total
    :return:
    """


def display_round_summary(players):
    """
    display_round_summary(players)
    Display the round summary, and check how much money each player has

    :param players: 2D dictionary of all players' data
    :return: the number of players who still have cash
    """