#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
Sultanov Andriy
"""
import string
import curses
from curses import wrapper
from edit_tree import Tree


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
    curses.curs_set(False)

    if curses.has_colors():
        curses.start_color()

    # Initialize a few main color pairs (foreground color, background color)
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
    curses.curs_set(True)
    curses.endwin()


def main(std_screen):
    """
    Main function of the module
    """
    tree = Tree()
    text = []

    # Add title and menu elements
    std_screen.addstr("Text Editor", curses.A_REVERSE | curses.color_pair(2))
    std_screen.addstr(curses.LINES - 1, 0,
                      "Press 'q' to exit, 'a' to undo, 's' to redo, 'e' to move a branch up, 'd' to move a branch down",
                      curses.A_REVERSE)

    # Create the editor window, draw the box around
    text_editor = curses.newwin(curses.LINES-14, curses.COLS, 1, 0)
    text_editor.box()

    # Create the sub-window for the actual text
    text_box = text_editor.subwin(curses.LINES-16, curses.COLS-4, 2, 2)

    # Create a window for drawing the tree of changes
    tree_window = curses.newwin(12, curses.COLS, curses.LINES - 13, 0)
    tree_window.box()

    tree_box = tree_window.subwin(10, curses.COLS-4, curses.LINES - 12, 2)

    # Refresh all the internal datastructures bottom-up, update the screen
    std_screen.noutrefresh()
    text_editor.noutrefresh()
    text_box.noutrefresh()
    tree_window.noutrefresh()
    tree_box.noutrefresh()
    curses.doupdate()

    possible_characters = string.ascii_letters + string.digits + string.punctuation + " \n"

    while True:
        char = text_editor.getkey()
        cur_pos = text_box.getyx()

        if char in ('q', 'Q'):

            # Quit the program
            break

        elif char in ('KEY_BACKSPACE', '\b', '\x7f'):

            # Get the current cursor position, delete teh character before it if there is any,
            # move to the previous lines if there is one
            if cur_pos[1] > 0:
                text_box.delch(cur_pos[0], cur_pos[1]-1)
            elif cur_pos[0] > 0:
                text_box.delch(cur_pos[0]-1, curses.COLS - 5)

            # Update the edit tree
            tree.add_node(text.pop(), False)

        elif char in ('a', 'A'):

            # Undo the last thing
            node = tree.move_back()

            if node is not None:
                if node.status:
                    text_box.delch(cur_pos[0], cur_pos[1]-1)
                else:
                    text_box.addch(node.char)

        elif char in ('s', 'S'):

            # Redo the last thing
            node = tree.move_forward()

            if node is not None:
                if node.status:
                    text_box.addch(node.char)
                else:
                    text_box.delch(cur_pos[0], cur_pos[1] - 1)

        elif char in ('e', 'E'):

            # Switch the branch upwards
            tree.move_branch_up()

        elif char in ('d', 'D'):

            # Switch the branch downwards
            tree.move_branch_down()

        elif char in possible_characters:

            # Update the edit tree and the character to the text_box
            text.append(char)
            tree.add_node(char, True)
            text_box.addch(char)

        tree_box.clear()
        tree_box.addstr(str(tree))

        std_screen.noutrefresh()
        text_editor.noutrefresh()
        text_box.noutrefresh()
        tree_window.noutrefresh()
        tree_box.noutrefresh()
        curses.doupdate()


if __name__ == '__main__':
    std_screen = start()
    wrapper(main)
    close(std_screen)
