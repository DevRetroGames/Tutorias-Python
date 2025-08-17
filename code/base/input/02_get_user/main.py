#!/usr/bin/env python3

from sys import exit
from math import sqrt

MSG_UNIC = "The result:"

OPERATIONS = {
    "+": lambda a, b: f"{MSG_UNIC} {a} + {b} = {a + b}",
    "-": lambda a, b: f"{MSG_UNIC} {a} - {b} = {a - b}",
    "*": lambda a, b: f"{MSG_UNIC} {a} * {b} = {a * b}",
    "/": lambda a, b: f"{MSG_UNIC} {a} / {b} = {a / b}",
    "**": lambda a, b: f"{MSG_UNIC} {a} ** {b} = {a ** b}",
    "%": lambda a, b: f"{MSG_UNIC} {a} % {b} = {a % b}",
    "//": lambda a, b: f"{MSG_UNIC} {a} // {b} = {a // b}",
    "sqrt": lambda a, b: f"{MSG_UNIC} sqrt {a} is {sqrt(a)} and sqrt {b} is {sqrt(b)}"
}

def _get_user_input(msg: str) -> str:
  return input(msg).strip().lower()
  
def _get_operation() -> str:
  msg: str = "Operations: +, -, *, /,**, %, //, sqrt.\nEnter operator: "
  return _get_user_input(msg)
  
def _get_value(value: str) -> int:
  msg: str = f"enter {value}"
  return int(_get_user_input(msg))
  
def _definir_resultado() -> str:
  operation: str = _get_operation()
  operation_no_cero = ["/", "%", "//"]

  msg_value_1: str = "first value: "
  value_1: int = _get_value(msg_value_1)

  msg_value_2: str = "second value: "
  value_2: int = _get_value(msg_value_2)

  while True:
    if operation in operation_no_cero and value_2 <= 0:
      print(f"second value can not cero")
      value_2= _get_value(msg_value_2)
    else:
      break

  return OPERATIONS[operation](value_1, value_2)
  
def main() -> None:
  try:
    print(_definir_resultado())
  except KeyboardInterrupt:
    print("\nOperation cancelled by user.")
    exit(0)

if __name__ == "__main__":
  main()