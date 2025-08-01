#!/usr/bin/env python3

import sys
from pathlib import Path

# Add the directory of the current script to the Python module search path
sys.path.append(str(Path(__file__).parent))

# Import the main function from the metric_mate module
from metric_mate import main as metric_mate_main

def main() -> None:
    # Call the imported main function to run the program
    metric_mate_main()

if __name__ == "__main__":
    # Entry point: execute main() when the script is run directly
    main()