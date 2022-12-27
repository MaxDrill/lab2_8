#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import sys


def get_input():
    """""
    requests keyboard input and returns the given string
    """""
    get_str = input("enter digit: ")
    return get_str

def test_input(a):
    """""
    checks if the given string can be transformed into a number. If yes, it returns yes.
    """""
    if type(a) == int or type(a) == float:
        return True
    elif a.isnumeric():
        return True
    else:
        return False


def str_to_int(b):
    """""
    converts transmitted meaning into int type 
    """""
    c = int(b)
    return c

def print_int(c):
    """""
    Displays the transmitted value on the screen 
    """""
    print(c)


if __name__== '__main__':
    s = get_input()
    bol = test_input(s)
    if bol:
        nmb = str_to_int(s)
        print_int(nmb)
    else:
        print(f"the entered value is not a number!", file=sys.stderr)