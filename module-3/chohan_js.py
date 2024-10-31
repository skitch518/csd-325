"""Cho-Han, by Al Sweigart al@inventwithpython.com
The traditional Japanese dice game of even-odd.
View this code athttps://nostarch.com/big-book-small-python-projects
Tags: short, beginner, game"""

import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.
''')

purse = 5000
while True:  # Main game loop.
    # Place your bet:
    # Added intials to output and formatted into f string so that if taking 12% produced a decimal it only displays a whole integer.
    print(f'You have {int(purse)} mon. How much do you bet? (or QUIT) JS: ')
    while True:
        pot = input('> ')
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            # This is a valid bet.
            pot = int(pot)  # Convert pot to an integer.
            break  # Exit the loop once a valid bet is placed.

    # Roll the dice.
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    # Let the player bet cho or han:
    while True:
        bet = input('> ').upper()
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    # Reveal the dice results:
    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    # Determine if the player won:
    rollIsEven = (dice1 + dice2) % 2 == 0
    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'
   # Added variables for the bonus
    bonus = 10
    award_bonus = False

    # Determine if the player recieves the bonus
    if dice1 + dice2 == 7 or dice1 + dice2 == 2:
        award_bonus = True
    else:
        award_bonus = False
        

    playerWon = bet == correctBet

    # Display the bet results:
    # Added an aditional check to see if the player won the bonus
    # Changed the percentage to 12%
    # Formatted outputs not to display a decimal
    if playerWon and award_bonus == True:
        print('You won! You take', pot, 'mon.')
        purse = purse + pot + bonus  # Add the pot from player's purse.
        print(f'You rolled a {dice1 + dice2} and won {bonus} mon.')
        print('The house collects a', pot * .12, 'mon fee.')
        purse = purse - (pot * .12)  # The house fee is 12%.
    elif playerWon:
        print('You won! You take', pot, 'mon.')
        purse = purse + pot  # Add the pot from player's purse.
        print(f'The house collects a {int(pot * .12)} mon fee.')
        purse = purse - (pot * .12)  # The house fee is 12%.
    else:
        purse = purse - pot  # Subtract the pot from player's purse.
        print('You lost!')

    # Check if the player has run out of money:
    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()