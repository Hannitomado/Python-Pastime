"""
Digital Stream, by Al Sweigart al@inventwithpython.com
A screensaver in the style of The Matrix movie's visuals.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: tiny, artistic, beginner, scrolling
"""

import random, shutil, sys, time

# Set up the constants:
MIN_STREAM_LENGTH = 6 # Can be modified ex. 1 or 50
MAX_STREAM_LENGTH = 14 # Can be modified ex. 100
PAUSE = 0.1 # Can be modified ex. 0.0 or 2.0
STREAM_CHARS = ['ア', 'イ', 'ウ', 'エ', 'オ', 'カ', 'キ', 'ク', 'ケ', 'コ', 'サ', 'シ', 'ス', 'セ', 'ソ', 
'タ', 'チ', 'ツ', 'テ', 'ト', 'ナ', 'ニ', 'ヌ', 'ネ', 'ノ', 'ハ', 'ヒ', 'フ', 'ヘ', 'ホ', 
'マ', 'ミ', 'ム', 'メ', 'モ', 'ヤ', 'ユ', 'ヨ', 'ラ', 'リ', 'ル', 'レ', 'ロ', 'ワ', 'ヲ', 'ン'] # Can be modified to other characters

# Density can range from 0.0 to 1.0:
DENSITY = 0.02 # Can be modified ex. 0.10 or 0.30

# Get the size of the terminal window:
WIDTH = shutil.get_terminal_size()[0]
# We can't print the last column on Windows without it addding a 
# newline automatically, so reduce the width by one:
WIDTH -= 1

print('Digital Stream, by Al Sweigart al@inventwithpython.com')
print('Press Ctrl-C to quit')
time.sleep(2)

try: 
    # For each column, when the counter is 0, no stream is shown.
    # Otherwise, it acts as a counter for how many times a 1 or 0
    # should be displayed in that column
    columns = [0] * WIDTH
    while True:
        # Set up the counter for each column:
        for i in range(WIDTH):
            if columns[i] == 0:
                if random.random() <= DENSITY:
                    # Restart a stream on this column
                    columns[i] = random.randint(MIN_STREAM_LENGTH,
                                                MAX_STREAM_LENGTH)
                    
            # Display an empty space or a 1/0 character.
            if columns[i] > 0:
                print('\033[92m' + random.choice(STREAM_CHARS) + '\033[0m', end='')
                columns[i] -= 1
            else:
                print('  ', end='')
        print() # Print a newline at the end of the row of columns.
        sys.stdout.flush() # Make sure text appears on the screen.
        time.sleep(PAUSE)
except KeyboardInterrupt:
    sys.exit() 