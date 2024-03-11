#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 10
    while i > 0:
        print(i)
        i -= 1
    if i == 0:
        print('Happy New Year!')

def square_integers(int_list):
    # code goes here!
    square_integers = []

    for element in int_list:
        square_integers += [(element * element)]
    return(square_integers)

def fizzbuzz():
    # code goes here!
    x = 1
    while x < 101:
        if x % 3 == 0 and x % 5 == 0:
            print('FizzBuzz')
        elif x % 3 == 0:
            print('Fizz')
        elif x % 5 ==0:
            print('Buzz')
        else:
            print(x)
        x += 1
    pass
