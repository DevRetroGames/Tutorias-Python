#!/usr/bin/env python3

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from check_modules import verify_from_file

def main() -> None:

    verify_from_file()

    from contact_book import ContactBook
    from message_loader import MessageLoader

    loader = MessageLoader(lang_code="en")
    messages = loader.get_messages()

    book = ContactBook(messages)

    try:
        book.run()
    except KeyboardInterrupt:
        print(f"\n{messages['messages']['operation_cancelled']}")
        sys.exit(0)

if __name__ == "__main__":
    main()