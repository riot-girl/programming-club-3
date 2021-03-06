#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
Level 3. Weekly Challenge 1: Generators

part a)
1. Read each line of the file with a generator
2. Iterate over the previous generator object and create a new generator with 
all the pair numbers.
3. Sum all values with a method of your choice.

"""

__author__ = "Pam Martínez"
__contact__ = "pamemart@cisco.com"
__copyright__ = "Copyright 2021, Cisco Systems"
__credits__ = ["MXC Programming Club, Daniel Medina"]
__date__ = "2021/03/03"
__deprecated__ = False
__email__ =  "pamemart@cisco.com"
__maintainer__ = "Pam Martínez"
__status__ = "Development"
__version__ = "0.0.1"

from time import time

def numbers_generator(name):
    # reading file 'name'
    file = open(name, 'r')
    # returning values row by row
    return (row for row in file)

def get_pairs(numbers):
    # this function will iterate over generator and create another only with 
    # the pair values
    return (number for number in numbers if int(number)%2 == 0)
       
# class get_pairs:
#     # iterator to pull pairs from numbers generator
#     def __init__(self, numbers):
#         self.numbers = numbers
#     def __iter__(self):
#         return self
#     def __next__(self):
#         # returning only the pair numbers
#         for number in self.numbers:
#             return number if int(number)%2 == 0 else 0
#         raise StopIteration

def add(numbers):
    # 'total' will acumulate the sum of values received
    total = 0
    # adding all the received values
    for number in numbers:
        total += int(number)
    return total

def main():
    start = time()
    numbers = numbers_generator('Numbers.csv')
    pairs = get_pairs(numbers)
    total = add(pairs)
    print(f"Total sum of pairs in file: {total}")
    end = time()
    print(f"Runtime 1: {end - start} seconds.")
    
if __name__ == "__main__":
    main()