#!/usr/bin/env python3

import re
import sys
from fractions import Fraction
from typing import Callable, Tuple

# Dictionary that maps conversion keys to a tuple of (origin unit, conversion function)
CONVERSIONS: dict[str, Tuple[str, Callable[[Fraction], Fraction]]] = {
    "cm": ("m", lambda x: x * 100),                  # meters to centimeters
    "cm_from_ft": ("ft", lambda x: x * Fraction("30.48")),  # feet to centimeters
    "kg": ("g", lambda x: x / 1000),                 # grams to kilograms
    "ft": ("in", lambda x: x / 12),                   # inches to feet
}

# Aliases to normalize different ways users might input units
ALIASES = {
    "g": "g",
    "gram": "g",
    "grams": "g",
    "kg": "kg",
    "kilogram": "kg",
    "kilograms": "kg",
    "kilo": "kg",
    "cm": "cm",
    "centimeter": "cm",
    "centimeters": "cm",
    "m": "m",
    "meter": "m",
    "meters": "m",
    "ft": "ft",
    "feet": "ft",
    "in": "in",
    "inch": "in",
    "inches": "in",
}

# Regex pattern to validate if the input string is a number (integer or decimal)
NUMBER_PATTERN = re.compile(r"^[0-9]+([.,][0-9]+)?$")


def _print_error_message() -> None:
    """Prints an error message for invalid number inputs."""
    print("Error: please enter only integers or decimals (using '.' or ',').")


def _process_value(value_str: str) -> Fraction:
    """
    Converts a string number with possible ',' decimal separator
    to a Fraction using '.' as decimal separator.
    """
    return Fraction(value_str.replace(",", "."))


def _is_valid_number(value_str: str) -> bool:
    """Checks if the input string matches the valid number pattern."""
    return bool(NUMBER_PATTERN.fullmatch(value_str))


def _get_user_input(prompt: str, input_type: str = "text") -> str | Tuple[str, Fraction]:
    """
    Gets input from the user.
    If input_type is 'number', validates and returns the input string and a Fraction.
    Otherwise, returns the input in lowercase.
    """
    while True:
        user_input = input(prompt).strip()

        if not user_input:
            print("Input cannot be empty. Please try again.")
            continue

        match input_type:
            case "number":
                if _is_valid_number(user_input):
                    return user_input, _process_value(user_input)
                _print_error_message()
            case _:
                return user_input.lower()


def _normalize_unit(unit: str) -> str | None:
    """
    Normalizes the unit string by lowercasing and removing dots and spaces,
    then looks it up in the ALIASES dictionary.
    Returns the normalized unit or None if not found.
    """
    unit_clean = unit.lower().strip().replace(".", "").replace(" ", "")
    return ALIASES.get(unit_clean)


def _show_units() -> None:
    """Prints the available conversions in a user-friendly format."""
    print("Available conversions:")
    for dest_unit, (origin_unit, _) in CONVERSIONS.items():
        # Remove prefix like 'cm_from_' to show target unit clearly
        print(f" - {origin_unit} → {dest_unit.removeprefix('cm_from_')}")


def _unsupported_unit_msg(unit: str, kind: str) -> None:
    print(f"\"{unit}\" is an unsupported {kind} unit")


def _validate_unit(unit: str, unit_type: str = "target") -> bool:
    """
    Validates if the given unit is supported.
    Prints an error message if not and returns False.
    Returns True if unit is supported.
    """
    if (normalized := _normalize_unit(unit)) is None:
        _unsupported_unit_msg(unit, unit_type)
        return False
    return True


def _try_convert(value_fraction: Fraction, origin_unit: str, target_unit: str, original_value: str) -> bool:
    """
    Attempts to perform the conversion.
    Prints the result if successful and returns True.
    Returns False if no conversion path is found.
    """
    for key, (conv_origin_unit, convert_func) in CONVERSIONS.items():
        key_base = key.split('_')[0]
        if origin_unit == conv_origin_unit and target_unit == key_base:
            result = convert_func(value_fraction)
            formatted_result = f"{float(result):.4f}".rstrip('0').rstrip('.')
            print(f"Result: {original_value} {origin_unit} = {formatted_result} {target_unit}")
            return True
    return False


def _convert_value() -> None:
    """
    Handles user input for value, origin unit and target unit,
    validates inputs, and tries to convert the value.
    """
    original_value, value_fraction = _get_user_input(
        "Enter the value to convert (e.g. 1000, 12.5, or 12,5): ", input_type="number"
    )
    user_origin_unit = _get_user_input("Enter the origin unit (e.g. m, g, ft): ")
    user_target_unit = _get_user_input("Enter the target unit (e.g. cm, kg, ft): ")

    if not _validate_unit(user_origin_unit, "origin"):
        return
    if not _validate_unit(user_target_unit, "target"):
        return

    origin_unit = _normalize_unit(user_origin_unit)
    target_unit = _normalize_unit(user_target_unit)

    if not _try_convert(value_fraction, origin_unit, target_unit, original_value):
        print(f"No conversion path from '{origin_unit}' to '{target_unit}' found.")


def main() -> None:
    """Main loop that allows up to 5 conversions or until user interrupts."""
    try:
        for i in range(5):
            _show_units()
            _convert_value()
            print(f"Chance user {i+1}/5", end="\n\n")
        print("You have used all 5 chances, please restart")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(0)