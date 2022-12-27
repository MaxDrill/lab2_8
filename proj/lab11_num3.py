#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


def multiply():
    """""
    multiplying digits while it is not 0 
    """""
    print("<<<Enter digits that will be multiplied>>>")
    res = 1
    while True:
        a = int(input(">>> "))
        if a == 0:
            break
        else:
            res *= a
    return res

if __name__ == '__main__':
     print('result is', multiply())