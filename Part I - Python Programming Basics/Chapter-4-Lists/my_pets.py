#!/usr/bin/env python
# -*- coding: utf-8 -*-

my_pets = ['Zophie', 'Pooka', 'Fat-tail']
name = input("Enter a pet name: ")
if name not in my_pets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')
