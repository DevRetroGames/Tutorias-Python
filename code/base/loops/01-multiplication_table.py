#!/usr/bin/env python3

import sys
import re

# Precompiled regex pattern to match positive integers (excluding zero)
_regex_positive_int = re.compile(r"[1-9]\d*")

# Constants to define the multiplication table range
TABLE_START = 1
TABLE_END = 12

def _input_user(msg: str) -> int:
    """
    Prompt the user for input and ensure it is a positive integer.
    
    Args:
        msg (str): The prompt message to display to the user.
    
    Returns:
        int: A validated positive integer input from the user.
    """
    while not (match := _regex_positive_int.fullmatch(user_input := input(msg))):
        print("Please enter a positive integer.")
    return int(user_input)

def _get_multiplication_table(number: int, start: int = TABLE_START, end: int = TABLE_END) -> list[str]:
    """
    Generate the multiplication table lines for a given number.
    
    Args:
        number (int): The base number for the multiplication table.
        start (int): Starting multiplier (default is TABLE_START).
        end (int): Ending multiplier (default is TABLE_END).
    
    Returns:
        list[str]: A list of formatted strings representing the table.
    """
    return [f"{number} x {i} = {number * i}" for i in range(start, end + 1)]

def _print_multiplication_table(lines: list[str]) -> None:
    """
    Print the multiplication table lines to the console.
    
    Args:
        lines (list[str]): The multiplication table lines to display.
    """
    print("Multiplication table:", *lines, sep="\n")

def main() -> None:
    """
    Main entry point of the script. Handles user input, generates and displays the table.
    """
    try:
        num = _input_user("Enter a positive integer: ")
        lines = _get_multiplication_table(num)
        _print_multiplication_table(lines)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(0)

if __name__ == "__main__":
    main()