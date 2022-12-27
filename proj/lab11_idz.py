#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def get_flight():
    dest = input("What destination do you need? ")
    numb = int(input("What number of the train? "))
    date = float(input("What time do you need? "))

    # creation of dictionary
    return {
        'destination': dest,
        'number_train': numb,
        'flight_date': date,
    }


def display_flights(train):
    if train:
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 18
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^18} |'.format(
                "№",
                "Destination",
                "Number of the train",
                "Flight Date"
            )
        )
        print(line)
        for i, item in enumerate(train, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:>18} |'.format(
                    i,
                    item.get('destination', ''),
                    item.get('number_train', ''),
                    item.get('flight_date', 0)
                )
            )
        print(line)
    else:
        print('list is empty')


def select_flights(train):
    t = input("enter your destination: ")
    count = 0
    for i in train:
        if i.get('destination') == t:
            count += 1
            print(
                '{:>4}: {} {} {}'.format(
                    count,
                    i.get('destination', ''),
                    i.get('flight_date'),
                    i.get("number_train")
                )
            )
    if count == 0:
        print("We couldn't find this destination")


def main():
    # list of the flights
    train = []

    # organization of an endless loop
    while True:
        info = input(">>> ").lower()
        if info == 'exit':
            break

        elif info == 'add':
            flight = get_flight()
            train.append(flight)
            if len(train) > 1:
                train.sort(key=lambda item: item.get('flight_date', ''))

        elif info == 'list':
            display_flights(train)

        elif info.startswith('select'):
            select_flights(train)

        elif info == 'help':
            print("command list:\n")
            print("add - add information about a flight;")
            print("list - display the flight schedule;")
            print("select <type> - select destination;")
            print("help - show reference;")
            print("exit - leave a program.")
        else:
            print(f"unknown command {info}", file=sys.stderr)


if __name__ == '__main__':
    main()