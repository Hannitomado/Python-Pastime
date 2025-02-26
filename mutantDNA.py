"""
Mutant DNA, by Hannibal Tomasson, is a minor tweak of the 
program DNA by Al Sweigart. In this variation of their original code, 
an extra X nucleotide is added to the helix animation. Inspired by 
Marvel's X-Men comic books.

DNA, by Al Sweigart al@inventwithpython.com
A simple animation of a DNA double-helix. Press Ctrl-C to stop.
Inspired by matoken https://asciinema.org/a/155441
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: short, artistic, scrolling, science
"""

import random, sys, time
from colorama import Fore, Style, init

# Initialize colorama for the colored nucleotide
init(autoreset=True)

PAUSE = 0.15

# These are the invididual rows of the DNA animation:
ROWS = [
    #123456789 <- Use this to measure the number of spaces:
    '         ##', # Index 0 has no {}
    '        #{}-{}#',
    '       #{}---{}#',
    '      #{}-----{}#',
    '     #{}------{}#',
    '    #{}------{}#',
    '    #{}-----{}#',
    '     #{}---{}#',
    '     #{}-{}#',
    '      ##', # Index 9 has no {}
    '     #{}-{}#',
    '     #{}---{}#',
    '    #{}-----{}#',
    '    #{}------{}#',
    '     #{}------{}#',
    '      #{}-----{}#',
    '       #{}---{}#',
    '        #{}-{}#']

def colorize_nucleotide(nucleotide):
    """
    Color 'X' in red, keeps other normal.
    """
    return f"{Fore.RED}{nucleotide}{Style.RESET_ALL}" if nucleotide == 'X'else nucleotide

try:
    print('Mutant DNA Animation, by Hannibal Tomasson')
    print('Press Ctrl-C to quit...')
    time.sleep(2)
    rowIndex = 0

    while True: # Main program loop
        # Increment rowIndex to draw next row:
        rowIndex = rowIndex + 1
        if rowIndex == len(ROWS):
            rowIndex = 0

        if rowIndex == 0 or rowIndex == 9:
            print(ROWS[rowIndex])
            continue
        
        # Select random nucleotide pairs, guanine-cytosine and 
        # adenine-thymine:
        randomSelection = random.randint(1, 6)
        if randomSelection == 1:
            leftNucleotide, rightNucleotide = 'A', 'T'
        elif randomSelection == 2:
            leftNucleotide, rightNucleotide = 'T', 'A'
        elif randomSelection == 3:
            leftNucleotide, rightNucleotide = 'C', 'G'
        elif randomSelection == 4:
            leftNucleotide, rightNucleotide = 'G', 'C'
        elif randomSelection == 5:
            leftNucleotide, rightNucleotide = 'X', 'T'
        elif randomSelection == 6:
            leftNucleotide, rightNucleotide = 'A', 'X'

        # Print the row.
        print(ROWS[rowIndex].format(colorize_nucleotide(leftNucleotide), colorize_nucleotide(rightNucleotide)))
        time.sleep(PAUSE)
except KeyboardInterrupt:
    sys.exit()
    