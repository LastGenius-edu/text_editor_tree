#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
Sultanov Andriy
"""
from edit_tree import Tree


def main():
    """
    Main test function
    :return:
    """
    tree = Tree()
    tree.add_node('a')
    tree.add_node('b')
    tree.add_node('c')
    tree.move_back()
    # print(tree._current_node)
    tree.add_node('d')
    # print(tree._current_node)
    tree.add_node('e')
    tree.add_node('f')
    tree.move_back()
    tree.move_back()
    tree.add_node('r')
    tree.add_node('t')
    tree.move_back()
    tree.move_back()
    tree.add_node('y')
    tree.add_node('u')
    tree.move_back()
    tree.move_back()
    print(tree)
    # print(tree._temporary_selection)
    tree.move_branch_down()
    tree.move_branch_down()
    tree.move_branch_up()
    # print(tree._temporary_selection)
    tree.move_forward()
    print(tree)


if __name__ == '__main__':
    main()
