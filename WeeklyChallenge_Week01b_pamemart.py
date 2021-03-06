#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
Level 3. Weekly Challenge 1: Generators

part b)
4. Perform the same steps from 1-3 without using generators, read lines of the 
file, save all pair numbers from file to a list and finally sum all the values
5. Get the runtime when using generators and using a list.

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

def gen_list(name):
    # reading file 'name'
    file = open(name, 'r')
    # 'list' will store all the numbers in the file
    list = []
    # appending all the pair values to the list
    for row in file:
        if int(row)%2 == 0:
            list.append(row)
    file.close()
    return list

def add(numbers):
    # 'total' will acumulate the sum of values received
    total = 0
    # adding all the received values
    for row in numbers:
        total += int(row)
    return total

def main():
    start = time()
    list = gen_list('Numbers.csv')
    total = add(list)
    print(f"Total sum of pairs in file: {total}")
    end = time()
    print(f"Runtime 2: {end - start} seconds.")
    
if __name__ == "__main__":
    main()