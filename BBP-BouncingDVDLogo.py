"""
Bouncing DVD Logo, by Al Sweigart al@inventwithpython.com
A bouncing DVD logo animation. You have to be "of a certain age" to
appreciate this. Press Ctrl-C to stop.

NOTE: Do not resize the terminal window while this program is running. 
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: short, artistic, bext.
"""

import sys, random, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
WIDTH, HEIGHT = bext.size()
# Given that we can't print to the last column on Windows
# without it adding a newline, we reduce the width by 1.
WIDTH -= 1

# Values for logo, which can be changed for ex between 1 to 100.
NUMBER_OF_LOGOS = 5
# Value for pause between frames, which can be changed for ex between 0.001 to 0.1.
PAUSE_AMOUNT = 0.2
# List of colors, which can be reduced.
COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

UP_RIGHT    = 'ur'
UP_LEFT     = 'ul'
DOWN_RIGHT  = 'dr'
DOWN_LEFT   = 'dl'
DIRECTIONS  = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)

# Key names for logo dictionaries:
COLOR = 'color'
X = 'x'
Y = 'y'
DIR = 'direction'

def main():
    bext.clear()
    
    # Generate some logos.
    logos = []
    for i in range(NUMBER_OF_LOGOS):
        logos.append({COLOR: random.choice(COLORS),
                      X: random.randint(1, WIDTH - 4),
                      Y: random.randint(1, HEIGHT - 4),
                      DIR: random.choice(DIRECTIONS)})
        if logos[-1][X] % 2 == 1:
            # Make sure X is even so it can hit the corner.
            logos[-1][X] -= 1
    # Count of how many times a logo hits a corner.
    cornerBounces = 0

    # Main program loop. 
    while True:
        # Handle each logo in the logos list.
        for logo in logos:
            # Erase the logo's current location:
            bext.goto(logo[X], logo[Y])
            print('    ', end='') 

            originalDirection = logo[DIR]

            # Check if the logo bounces off the corners:
            if logo[X] == 0 and logo[Y] == 0:
                logo[DIR] = DOWN_RIGHT
                cornerBounces += 1
            elif logo[X] == 0 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_RIGHT
                cornerBounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == 0:
                logo[DIR] = DOWN_LEFT
                cornerBounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_LEFT
                cornerBounces += 1

            # Check if the logo bounces off the left edge:
            elif logo[X] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = UP_RIGHT
            elif logo[X] == 0 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = DOWN_RIGHT

            # Check if the logo bounces off the right edge:
            # We use WIDTH - 3 because the logo is 3 characters wide.
            elif logo[X] == WIDTH - 3 and logo [DIR] == UP_RIGHT:
                logo[DIR] = UP_LEFT
            elif logo[X] == WIDTH - 3 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = DOWN_LEFT

            # Check if the logo bounces of the top edge:
            elif logo[Y] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = DOWN_LEFT
            elif logo[Y] == 0 and logo[DIR] == UP_RIGHT:
                logo[DIR] = DOWN_RIGHT

            # Check if the logo bounces off the bottom edge:
            elif logo[Y] >= HEIGHT - 1 and (logo[DIR] == DOWN_LEFT or logo[DIR] == DOWN_RIGHT):
                logo[DIR] = UP_LEFT if logo[DIR] == DOWN_LEFT else UP_RIGHT
                logo[Y] = HEIGHT - 2  # Prevent out-of-bounds


            if logo[DIR] != originalDirection:
                # Change color when the logo bounces.
                logo[COLOR] = random.choice(COLORS)

            # Move the logo. (X moves by 2 because the terminal
            # characters are twice as tall as they are wide.)
            if logo[DIR] == UP_RIGHT:
                logo[X] += 2
                logo[Y] = min(HEIGHT - 1, logo[Y] + 1)
            elif logo[DIR] == UP_LEFT:
                logo[X] -= 2
                logo[Y] = min(HEIGHT - 1, logo[Y] + 1)
            elif logo[DIR] == DOWN_RIGHT:
                logo[X] += 2
                logo[Y] = max(0, logo[Y] - 1)
            elif logo[DIR] == DOWN_LEFT:
                logo[X] -= 2
                logo[Y] = max(0, logo[Y] - 1)

        # Display the number of corner bounces:
        bext.goto(5, 0)
        bext.fg('white')
        print('Corner bounces:', cornerBounces, end='')

        for logo in logos:
            # Draw the logo at its new location:
            bext.goto(logo[X], logo[Y])
            bext.fg(logo[COLOR])
            print('DVD', end='')

        bext.goto(0, 0)

        # Required for bext-using programs.
        sys.stdout.flush()
        time.sleep(PAUSE_AMOUNT)

# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Bouncing DVD Logo, by Al Sweigart')
        # When Ctrl=C is pressed, end the program.
        sys.exit() 