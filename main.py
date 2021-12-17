#!/usr/bin/env python3
"""
NAME
    main_menu - Chapter 6 Assignment

DESCRIPTION
    Student Data System for managing student information (student id, first name, and last name)

    This module contains the functions for displaying the main menu and running the menu options

FUNCTIONS
    display_menu()
        Displays a list of all the valid main menu options
        It also handles for nonnumerical data and invalid menu option selected.

        1 - List all students
        2 - Add a student
        3 - Update a student
        4 - Delete a student
        0 - Exit program

        :return: no value
        :rtype: none

    main()
        Main keeps the program looping until the user enters 0 to exit the program
        then based on the user's selected, will call the corresponding function option
        Local scoped students is a 2D list that is pass as an argument to each menu option function
        Local scoped max_student_id is the last student id used, and is passed to the add_student function,
        and this function will return the last added student id

        :return: no value
        :rtype: none

VERSION
    1.0

DATE
    2021.10.31

AUTHOR
    Penelope Harding
"""


import game21 as game

LINE_LENGTH = 28


def play_game():
    """
    play_game()
    Main outer while loop to keep playing rounds

    :return: n/a
    """

    while True:
        break
    print("later skater")
    input('Press the enter key to continue...')


if __name__ == "__main__":
    play_game()
