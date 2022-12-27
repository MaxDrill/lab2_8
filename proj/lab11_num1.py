#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import sys

def test():
    """
    inputing a digit and checking the meaning """
    dig = int(input('enter positive or negative digit: '))
    if dig >= 0:
        positive()
    else:
        negative()

def positive():
    """
    output to the screen """
    print('positive')


def negative():
    """
    output to the screen """
    print('negative')


if __name__ == '__main__':
    test()