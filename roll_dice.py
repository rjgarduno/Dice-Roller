# Script to Roll Dice
# Parameters:
#   Number of dice to be rolled
#   Number of sides per dice.
# Output:
#   List of length "diceNumber" of rolled dice with "diceSides" number of sides.

import random

#~~~~~~ VARIABLES: ~~~~~~#

diceNumber = int(input("Please enter the number of dice you want to roll: "))

diceSides = int(input("Please enter the number of sides per dice: "))

print("Now rolling {}d{}...".format(diceNumber, diceSides))

#~~~~~~ FUNCTIONS: ~~~~~~#

def rollDice(diceNumber, diceSides):
    diceResults = []
    for i in range(diceNumber):
        rolledDice = random.randint(1, diceSides)
        diceResults.append(rolledDice)
    return diceResults

#~~~~~ MAIN BLOCK: ~~~~~~#

diceValues = rollDice(diceNumber, diceSides)
rollTotal = sum(diceValues)

print("You have rolled {} for a total of {}.".format(diceValues, rollTotal))

input("Press ENTER to close this script.")