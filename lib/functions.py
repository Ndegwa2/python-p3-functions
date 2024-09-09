#!/usr/bin/env python3

def greet_programmer():
    """Output a greeting to the programmer."""
    print("Hello, programmer!")


def greet(name):
    """Output a personalized greeting to the provided name."""
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    """Output a greeting with a default name if no argument is provided."""
    print(f"Hello, {name}!")

def add(num1, num2):
    """Return the sum of two numbers."""
    return num1 + num2

def halve(num):
    """Return the value of the number divided by two."""
    return num / 2
