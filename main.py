#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
Sultanov Andriy
"""
import curses
from curses import wrapper
from time import sleep


def start():
    """
    Starts the screen
    """
    std_screen = curses.initscr()

    # Setting up the curses module so that keys would not be echoed instantly to the screen
    curses.noecho()
    # Shifting from standard buffer mode to instant action on key press
    curses.cbreak()
    # Turning on keypad mode for easier custom keys support
    std_screen.keypad(True)

    curses.curs_set(False)

    if curses.has_colors():
        curses.start_color()

    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)

    return std_screen


def close(std_screen):
    """
    Closes the curses application
    """
    curses.echo()
    curses.nocbreak()
    std_screen.keypad(False)
    curses.endwin()


def main(std_screen):
    """
    Main function of the module
    """
    sleep(3)
    std_screen.addstr("Text Editor", curses.A_REVERSE)
    std_screen.chgat(-1, curses.A_REVERSE)
    std_screen.refresh()
    sleep(3)


if __name__ == '__main__':
    std_screen = start()
    main(std_screen)
    close(std_screen)
