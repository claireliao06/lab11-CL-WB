"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def add(a, b):
    a + b

def subtract(a, b):
    a - b

def multiply(a, b):
    a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a

def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Invalid base")
    if b <= 0:
        raise ValueError("Invalid argument")
    return math.log(b, a)# use math library/raise ValueError

def exponent(a, b):
    return a ** b



