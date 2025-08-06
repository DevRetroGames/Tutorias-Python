#!/usr/bin/env python3

import sys
import random
import time

START = 1
END = 2
MESSAGES = [
    "Espera...",
    "Un momento...",
    "Espera un segundo...",
    "Creo que ya lo tengo."
]
DELAYS = [2, 3, 1, 5]

def _random_value() -> int:
    return random.randint(START, END)

def _dramatic_wait(msg: str, delay: int) -> None:
    print(msg)
    time.sleep(delay)

def _flip_coin() -> str:
    return "Cara" if _random_value() == 1 else "Cruz"

def main() -> None:
    try:
        for msg, delay in zip(MESSAGES, DELAYS):
            _dramatic_wait(msg, delay)
        
        print(f"Result: {_flip_coin()}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(0)

if __name__ == "__main__":
    main()