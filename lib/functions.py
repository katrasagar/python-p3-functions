#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")


def greet(name):
   print(f"Hello, {name}!")
greet("katra")   

def greet_with_default(name="programmer"):
   print(f"Hello, {name}!")
greet_with_default()

def add(num1, num2):
    return num1 + num2
    result = add(1, 2)
    print(result)  


def halve(number):
    return number /2
    result = halve(6)
    print(result)
