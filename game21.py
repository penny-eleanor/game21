#!/usr/bin/env python3

import random

LINE_LENGTH = 40


def get_yn_input(prompt):
    """
    get_yn_input(prompt)
    Displays a yes/no prompt and returns with either y or n

    :param prompt:
    :return: the user's response (y/n)
    """
    # prompt = message that goes before the user prompt when called.
    while True:
        user_input = input(f'{prompt}')
        if user_input == 'y' or user_input == 'n':
            return user_input
        else:
            print('Please enter a valid response (y/n).')


def display_game_intro():
    """
    display_game_intro()
    Displays the game title and the rules of the game

    :return: n/a
    """
    print(LINE_LENGTH * '=')
    print('\t\t ~*~ Welcome to Game 21 ~*~')
    print(LINE_LENGTH * '=')
    print('The rules are simple!')
    print('\t1. Each player is trying to get as close to 21 without going over.')
    print('\t2. Each player is ONLY trying to beat the dealer\'s hand.')
    print('\t3. The dealer will keep dealing himself cards until he beats all players hands or goes over 21.')
    print('\t4. Tie goes to the player, not the dealer.')
    print('\t5. Each player gets dealt two card between 1 - 10.')
    print('\t6. The player then can choose to receive additional cards.')
    print('\t7. Each player starts with $1.00.')
    print('\t8. Default bet is 25 cents, but the player can double it after holding.')
    print('\t9. Winner is the last person with cash, not including the dealer.')
    print('\t10. Have fun! :)')
    print(LINE_LENGTH * '-')


def get_players():
    """
    get_players()
    Gets the players names, adding them to the dictionary and setting initial data
    Stops when user enters the word 'done'
        set cash to $1.0
        set cards to an empty list
        set cards_total to 0
        set bet to 0.25 default value

    :return: 2D dictionary of all players' data
    """
    players = {}

    print('Who\'s all playing?')
    print('Enter each player\'s name, and enter \'done\' when finished.')

    while True:
        player_name = input('Enter name: ')

        if player_name > '' and player_name != 'done':
            players[player_name] = {
                'cash': 1.0,
                'cards': [],
                'cards_total': 0,
                'bet': 0.25
            }
        elif player_name == 'done':
            break
        else:
            print('Invalid input: Please enter a value')

    print(LINE_LENGTH * '=')
    print('\t\t Starting game...')
    print(LINE_LENGTH * '=')

    return players


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
    setup_new_round(players)
    deal_to_players(players)
    dealer_cards_total = deal_to_dealer(players)
    display_winners(players, dealer_cards_total)


def setup_new_round(players):
    """
    setup_new_round(players)
    Reset all player's data for the next round.
        set cards to an empty list
        set cards_total to 0
        set bet to 0.25 default value

    :param players: 2D dictionary of all players' data
    :return: n/a
    """
    for player_name, player_info in players.items():
        player_info['cards'] = []  # initialize the player's hand as being empty
        player_info['cards_total'] = 0  # initialize the player's hand as having a total value of 0
        player_info['bet'] = 0.25  # each player's current bet starts off undoubled at 25 cents


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
    card = random.randint(1, 10)  # get a random number between 1 and 10 inclusive
    player_info['cards'].append(card)  # add the card to the player's list of cards
    player_info['cards_total'] += card  # add the card value to the player's cards_total


def double_bet(player_info):
    """
    deal_card(player_info)
    Doubles the player's bet from 0.25 to 0.50

    :param player_info: 2D dictionary of all players' data
    :return: n/a
    """
    player_info['bet'] = 0.50  # sets the player's bet to 50 cents


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
    for player_name, player_info in players.items():
        cash, cards, cards_total, bet = player_info.values()

        if cash < 0.25:
            continue

        print('Dealing to ' + player_name)

        # deal the first two cards to the current player
        deal_card(player_info)
        deal_card(player_info)

        # unpack the sub dictionary again - the player's cards have changed
        cash, cards, cards_total, bet = player_info.values()
        display_cards(cards)

        another_card = get_yn_input(prompt=" Do you want another card? (y/n): ")
        while another_card == 'y':
            deal_card(player_info)

            cash, cards, cards_total, bet = player_info.values()
            display_cards(cards)
            another_card = get_yn_input(prompt=" Do you want another card? (y/n): ")

        print(' ', player_name, 'holds at', cards_total)
        double_prompt = get_yn_input(prompt=" Do you want double your 25 cent bet? (y/n): ")
        if double_prompt == 'y':
            double_bet(player_info)
        print()


def deal_to_dealer(players):
    """
    deal_to_dealer(players)
    If there are no players still playing this hand (they did not exceed 21)
    then the dealer automatically wins
    Otherwise start dealing to the dealer until he beats all players or reaches 21

    :param players: 2D dictionary of all players' data
    :return: dealer_cards_total: total value of dealer's hand
    """
    num_players_out = 0
    highest_hand = 0

    # need to determine if there are any players still in the round or if they all exceeded 21
    for player, player_info in players.items():  # get the player_name (key) and player_info (value)
        cards_total = player_info['cards_total']
        if cards_total > 21:
            num_players_out += 1
        elif cards_total > highest_hand:
            highest_hand = cards_total

    # if there are no players left in this round
    # then there is no point dealing to the dealer, because the dealer automatically wins
    if num_players_out == len(players):
        return 21  # returning 21 will make the dealer automatically win

    # if there are still players in the round, we deal to the dealer
    print('Dealing to dealer.')

    dealer_cards = []
    dealer_cards_total = 0

    # deal to the dealer one card at a time until...
    # ... the dealer beats all players
    # ... the dealer reaches 21
    # ... the dealer exceeds 21
    while True:
        card = random.randint(1, 10)
        dealer_cards.append(card)
        dealer_cards_total += card

        if dealer_cards_total > 21:
            display_cards(dealer_cards)
            print(' Dealer\'s hand exceeded 21')
            return dealer_cards_total
        elif dealer_cards_total >= highest_hand:
            display_cards(dealer_cards)
            print(' Dealer holds at', dealer_cards_total)
            return dealer_cards_total


def display_cards(cards):
    """
    display_cards(cards)
    Display one player's current list of cards on one line

    :param cards: one player's current cards
    :return: n/a
    """
    print(' Cards: ', end='')
    for card in cards:
        print(str(card) + ' ', end='')
    print()


def display_winners(players, dealer_cards_total):
    """
    display_winners(players, dealer_cards_total)
    Display the winners for the current round

    :param players: 2D dictionary of all players' data
    :param dealer_cards_total: total value of dealer's hand
    :return:
    """
    total_winners = 0  # used to determine if the dealer is the automatic winner

    for player_name, player_info in players.items():  # get the player_name (key) and player_info (value)

        cash, cards, cards_total, bet = player_info.values()  # unpack the current player's data

        if cash < 0.25:  # player is out of the game because they are broke
            continue

        if dealer_cards_total > 21:  # dealer exceeded 21
            if cards_total <= 21:  # as long as the player is still in the game
                total_winners += 1
                player_info['cash'] += bet  # player won, add their bet to their cash
                print('$', player_name, 'won! $')
            else:
                player_info['cash'] -= bet  # player lost, subtract their bet from their cash
        else:
            player_info['cash'] -= bet  # player lost, subtract their bet from their cash


def display_round_summary(players):
    """
    display_round_summary(players)
    Display the round summary, and check how much money each player has

    :param players: 2D dictionary of all players' data
    :return: the number of players who still have cash
    """
    print(LINE_LENGTH * '-')
    print('\t End of Round Summary')
    print(LINE_LENGTH * '-')

    for player_name, player_info in players.items():  # get the player_name (key) and player_info (value)

        cash, cards, cards_total, bet = player_info.values()

        if cash >= .25:
            print('$', cash, '\t', player_name, '\'s balance')
        else:
            print(player_name, 'is flat broke.')
