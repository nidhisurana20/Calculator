"""A simple command-line calculator supporting basic arithmetic operations."""

import math
import sys


class CalculatorError(Exception):
    """Raised for calculator-specific errors (e.g. divide by zero)."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise CalculatorError("Cannot divide by zero.")
    return a / b


def power(a, b):
    return a ** b


def sqrt(a):
    if a < 0:
        raise CalculatorError("Cannot take square root of a negative number.")
    return math.sqrt(a)


OPERATIONS = {
    "1": ("Add", add, 2),
    "2": ("Subtract", subtract, 2),
    "3": ("Multiply", multiply, 2),
    "4": ("Divide", divide, 2),
    "5": ("Power (a^b)", power, 2),
    "6": ("Square root", sqrt, 1),
}


def prompt_number(label):
    while True:
        raw = input(f"Enter {label}: ").strip()
        try:
            return float(raw)
        except ValueError:
            print("  Invalid number, try again.")


def run_menu():
    print("=== Simple Calculator ===")
    for key, (name, _, _) in OPERATIONS.items():
        print(f"  {key}. {name}")
    print("  0. Quit")

    while True:
        choice = input("\nChoose an operation: ").strip()
        if choice == "0":
            print("Goodbye.")
            break
        if choice not in OPERATIONS:
            print("  Invalid choice, try again.")
            continue

        name, func, arity = OPERATIONS[choice]
        try:
            if arity == 2:
                a = prompt_number("first number")
                b = prompt_number("second number")
                result = func(a, b)
            else:
                a = prompt_number("number")
                result = func(a)
            print(f"  Result: {result}")
        except CalculatorError as e:
            print(f"  Error: {e}")


if __name__ == "__main__":
    try:
        run_menu()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye.")
        sys.exit(0)
