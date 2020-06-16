#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
Sultanov Andriy
"""
import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
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
    # Turning the flickering pointer off
    # curses.curs_set(False)

    if curses.has_colors():
        curses.start_color()

    # Initialize a few main color pairs (foreground color, backround color)
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
    # curses.curs_set(True)
    curses.endwin()


def main(std_screen):
    """
    Main function of the module
    """

    # Add title and menu elements
    std_screen.addstr("Text Editor", curses.A_REVERSE | curses.color_pair(2))
    std_screen.chgat(-1, curses.A_REVERSE | curses.color_pair(2))
    std_screen.addstr(curses.LINES - 1, 0, "Press 'q' to exit", curses.A_REVERSE)

    # Create the editor window, draw the box around
    text_editor = curses.newwin(curses.LINES - 2, curses.COLS, 1, 0)
    text_editor.box()

    # Create the subwindow for the actual text
    text_box = text_editor.subwin(curses.LINES-4, curses.COLS-4, 2, 2)

    # Refresh all the internal datastructures bottomup, update the screen
    std_screen.noutrefresh()
    text_editor.noutrefresh()
    text_box.noutrefresh()
    curses.doupdate()

    box = Textbox(text_box)
    box.edit()

    # while True:
    #     char = text_editor.getch()
    #
    #     if char in (ord('q'), ord('Q')):
    #         break
    #     else:
    #         text_box.addch(char)
    #
    #     std_screen.noutrefresh()
    #     text_editor.noutrefresh()
    #     text_box.noutrefresh()
    #     curses.doupdate()


if __name__ == '__main__':
    std_screen = start()
    main(std_screen)
    close(std_screen)
