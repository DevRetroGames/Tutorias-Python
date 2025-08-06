#!/usr/bin/env python3

import sys
from pathlib import Path

# Add the current script's directory to the system path
# This allows importing local modules from the same directory
sys.path.append(str(Path(__file__).parent))

# Import a function that verifies required modules from a file
from check_modules import verify_from_file

def main() -> None:
    # Verify that all required Python modules are installed
    verify_from_file()

    # Import local modules after verification is done
    from message_loader import MessageLoader
    from investment_simulator import InvestmentSimulator

    # Load localized messages (e.g., English or Spanish) from a YAML file
    loader = MessageLoader(lang_code="en")
    messages = loader.get_messages()

    # Create an instance of the investment simulator with the loaded messages
    investment = InvestmentSimulator(messages)

    try:
        # Start the investment simulation process
        investment.run()
    except KeyboardInterrupt:
        # Gracefully handle the user pressing Ctrl+C (KeyboardInterrupt)
        print(f"\n{messages['messages']['operation_cancelled']}")
        sys.exit(0)

# Entry point: run the main function when this file is executed directly
if __name__ == "__main__":
    main()