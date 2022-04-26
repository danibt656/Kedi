#!/usr/bin/python3
"""
    Kedi is an enhanced version of the cat command, inspired by batcat
    
    Daniel Barahona 2022
"""

import os
import sys

MARGIN = 8

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   GRAY = '\033[1;30;40m'
   LIGHT_GRAY = '\033[0;37;40m'
   END = '\033[0m'

def print_window_top(size):
    print(color.GRAY+'┌──────┬', end='')
    for i in range(0, size-9):
        print('─', end='')
    print('┐'+color.END)

def print_window_end(size):
    print(color.GRAY+'└──────┴', end='')
    for i in range(0, size-9):
        print('─', end='')
    print('┘'+color.END)

def print_line(size, line_num, line_txt):
    print(color.GRAY+'│'+color.END+color.BOLD+'{:>5}'.format(f'{line_num}')+color.GRAY+' │ '+color.END, end='')
    i,j = 0,0
    total_space = size - size//MARGIN
    total_chars = len(line_txt)
    while i < total_chars:
        j = 0
        while j < total_space and i < total_chars:
            print(f'{line_txt[i]}', end='')
            i += 1
            j += 1
        if i < total_chars:
            print('\n'+color.GRAY+'│'+color.END+color.BOLD+'{:>5}'.format(' ')+color.GRAY+' │ '+color.END, end='')

def main():
    term_cols = os.get_terminal_size().columns
    filename = sys.argv[1]
    
    # Print file name and box top
    print(f'\t\033[93m{color.BOLD}{filename}{color.END}')
    print_window_top(term_cols)
    # Print file lines
    with open(filename, 'r') as f:
        lines = f.readlines()
        lnum = 0
        for line in lines:
            lnum += 1
            print_line(term_cols, lnum, line)
    # Print box bottom
    print_window_end(term_cols)

if __name__ == '__main__':
    main()
