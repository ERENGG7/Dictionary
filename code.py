# -*- coding: utf-8 -*-

import time
import os

my_dictionary = {
    1:["Cola"],
    2:["Pepsi"],
    3:["Sprite"],
    4:["Martini"],
    5:["Aperol"],
    6:["Water"]
}

def get_value():
    for key, value in my_dictionary.items():
       print(f"{key}: {value}")

def add_to_list(lst):
    while True:
       os.system("cls")
       get_value()
       n = input("Enter number of key to add to list: ")
       if n == "esc":
           break
       a = int(n)
       if a in my_dictionary:
          lst.append(my_dictionary[a][0])
          continue
       print("Invalid1 choice!")
       time.sleep(2)

def print_items(lst):
    for n in lst:
        print(n)
def program():
    lst = []
    add_to_list(lst)
    print_items(lst)
program()