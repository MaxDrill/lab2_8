#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import math

def cylinder():
    """""
    calculation of the full or side square cylinder
    """""
    while True:
        option = int(input("<<<What kind of square do you want tocalculate?>>>\n"
                        "1 - Side surface\n" 
                        "2 - Full surface\n" 
                        ">>> "))
        if (option != 1) and (option != 2):
            print('unknown command')
            break
        r = int(input("Enter the radius: "))
        h = int(input("Enter the height of the cylinder: "))
        if option == 1:
            s = 2 * math.pi * r * h
            print("S(side.) = ", '{:.3f}'.format(s))
            break
        else:
            s = (2 * math.pi * r * h) + (circle(r) * 2)
            print("S(full.) = ", '{:.3f}'.format(s))
            break

def circle(r):
    """""
    Calculation of the square of the circle by a given radius
    """""
    return math.pi * (r ** 2)

if __name__ == '__main__':
    cylinder()