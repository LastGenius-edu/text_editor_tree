#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
Sultanov Andriy
"""


class Node:
    """
    Node class of one single-character edit
    """

    def __init__(self, char, status=True, parent=None, children=None):
        """
        Creates a single-character edit instance with children

        :param char: str
        :param children: list
        """
        self.char = char
        self.status = status
        self.parent = parent
        self.children = [] if children is None else children

    def __str__(self):
        """
        Returns a string representation of a node
        :return: str
        """
        return f"{'+' if self.status else '-'}{self.char}"


class Tree:
    """
    Edit Tree class
    """

    def __init__(self):
        """
        Initializes an empty tree of edits
        """
        self._root = Node('root', True)
        self._current_node = None
        self._temporary_selection = 0

    def add_node(self, char, status):
        """
        Adds a node to the tree. If needed, creates a new branch.
        :return: None
        """
        if self._current_node is None:
            node = Node(char, status, parent=self._root)
            self._root.children.append(node)
        else:
            node = Node(char, status, self._current_node)
            self._current_node.children.append(node)

        self._current_node = node

    def move_back(self):
        """
        Changes the current node to the previous one, if there is such
        :return:
        """
        if self._current_node is not None and self._current_node.char != 'root':
            node = self._current_node
            self._current_node = self._current_node.parent
            return node

    def move_forward(self):
        """
        Changes the current node to the next one, if there is such
        :return:
        """
        if self._current_node.children:
            self._current_node = self._current_node.children[self._temporary_selection]
            self._temporary_selection = 0
            return self._current_node

    def move_branch_up(self):
        """
        Changes the current branch to the upper one, if there is such
        :return:
        """
        if self._temporary_selection > 0:
            self._temporary_selection -= 1

    def move_branch_down(self):
        """
        Changes the current branch to the lower one, if there is such
        :return:
        """
        if len(self._current_node.children) > (self._temporary_selection + 1):
            self._temporary_selection += 1

    def __str__(self):
        """
        Returns a string representation of a part of the tree
        :return: str
        """
        final_result = ""
        if self._current_node is not None:
            if self._current_node.char != 'root':
                final_result += f"Undo: {self._current_node}"

            if self._current_node.children:
                final_result += f" Redo: {self._current_node.children[0]}"

            final_result += "\n"

        if self._current_node is not None and self._current_node.parent is not None:
            final_result += f"{self._current_node.parent}=="

        def print_line(node):
            result = ""

            while True:
                result += str(node) + "=="
                if node is not None and node.children:
                    node = node.children[0]
                else:
                    break

            return result

        if self._current_node is not None:
            final_result += print_line(self._current_node) + "\n"
            branches = [f"    |={print_line(child)}" for child in self._current_node.children[1:]]
            if self._temporary_selection != 0:
                branches[self._temporary_selection - 1] = f"- - {branches[self._temporary_selection - 1][4:]}"
            final_result += '\n'.join(branches)

        return final_result
