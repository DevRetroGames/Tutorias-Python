#!/usr/bin/env python3

from typing import Tuple

class ContactBook:
    def __init__(self, messages: dict):
        self._contacts = {
            "sanskar": ["(+91) 0123456789"],
            "jacob": ["(+1) 9876543210"],
            "charles": ["(+1) 4728450681"],
            "rohan": ["(+91) 4200065820"],
            "william": ["(+44) 8265710268"]
        }
        self._messages = messages

    def _input_user(self, msg: str) -> str:
        return input(msg).strip().lower()

    def _search_contact(self, name: str) -> bool:
        return name in self._contacts

    def _print_contacts(self) -> None:
        for name, phones in self._contacts.items():
            print(f"{name.title()}: {', '.join(phones)}")

    def _print_contact(self, name: str) -> None:
        phones = self._contacts.get(name)
        if phones:
            print(self._messages["contacts"]["show"].format(name=name.title(), phones=', '.join(phones)))
        else:
            print(self._messages["contacts"]["not_found"].format(name=name.title()))

    def _get_contact(self) -> Tuple[str, str]:
        name = self._input_user(self._messages["prompts"]["enter_name"])
        phone = self._input_user(self._messages["prompts"]["enter_number"])
        return name, phone

    def _get_phone(self) -> str:
        return self._input_user(self._messages["prompts"]["enter_number"])

    def _add_contact(self, name: str, phone: str) -> None:
        self._contacts[name] = [phone]

    def _add_phone_to_contact(self, name: str, phone: str) -> None:
        if phone not in self._contacts[name]:
            self._contacts[name].append(phone)

    def _show_menu(self) -> None:
        print('\n'.join(self._messages["menu"]))

    def _handle_show_contacts(self) -> None:
        print(self._messages["messages"]["contacts_list"])
        self._print_contacts()

    def _handle_search_contact(self) -> None:
        name = self._input_user(self._messages["prompts"]["search_name"])
        self._print_contact(name)

    def _handle_add_contact(self) -> None:
        name, phone = self._get_contact()
        self._add_contact(name, phone)
        print(self._messages["messages"]["contact_added"])

    def _handle_add_phone(self) -> None:
        name = self._input_user(self._messages["prompts"]["contact_name"])
        if self._search_contact(name):
            phone = self._get_phone()
            self._add_phone_to_contact(name, phone)
            print(self._messages["messages"]["number_added"])
        else:
            print(self._messages["messages"]["contact_not_found"])

    def _handle_exit(self) -> bool:
        print(self._messages["messages"]["exiting"])
        return False

    def _handle_invalid_option(self) -> None:
        print(self._messages["messages"]["invalid_option"])

    def run(self) -> None:
        actions = {
            "1": self._handle_show_contacts,
            "2": self._handle_search_contact,
            "3": self._handle_add_contact,
            "4": self._handle_add_phone,
            "5": self._handle_exit,
        }

        while True:
            self._show_menu()
            option = self._input_user(self._messages["prompts"]["select_option"]).strip()

            action = actions.get(option, self._handle_invalid_option)
            if action() is False:
                break