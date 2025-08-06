#!/usr/bin/env python3

import sys
from pathlib import Path

# Add the current script's directory to the system path so local modules can be imported
sys.path.append(str(Path(__file__).parent))

# Import function to verify and install required Python modules
from check_modules import verify_from_file

def main() -> None:
    # Verify required modules from the requirements.txt file
    verify_from_file()

    # Import project modules after ensuring dependencies are installed
    from contact_book import ContactBook
    from message_loader import MessageLoader

    # Load localized messages using the English language code
    loader = MessageLoader(lang_code="en")
    messages = loader.get_messages()

    # Create an instance of ContactBook with the loaded messages
    book = ContactBook(messages)

    try:
        # Run the main functionality of the contact book
        book.run()
    except KeyboardInterrupt:
        # Gracefully handle a keyboard interruption (Ctrl+C)
        print(f"\n{messages['messages']['operation_cancelled']}")
        sys.exit(0)

# Entry point of the script
if __name__ == "__main__":
    main()