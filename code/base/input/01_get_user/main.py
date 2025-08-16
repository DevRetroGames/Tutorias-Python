#!/usr/bin/env python3

import sys

user_dict: dict = {
  "name": "",
  "hobbies": "",
  "career": "",
  "music": ""
}

msg_input_dict: dict = {
  "name": "What is your name?: ",
  "hobbies": "What are your hobbies?: ",
  "career": "What career do you want when you grow up?: ",
  "music": "What kind of music do you listen to?: "
}

msg_print_dict: dict = {
  "name": "It is nice to meet you, {}",
  "hobbies": "Thoese are very cool hobbies, {}",
  "career": "That's a very cool career choice, {}",
  "music": "Those are very cool genres of music, {}"
}

item_list: list = ["name", "hobbies", "career", "music"]

def _get_user_input(msg: str) -> str:
  input(msg)
  
def _set_user_dict(key: str, value: str) -> None:
  user_dict[key] = value
  
def _get_data(key: str, msg: str) -> None:
  data: str = _get_user_input(msg)
  _set_user_dict(key, data)

def _set_data() -> None:
  for item in item_list:
    _get_data(item, msg_input_dict[item])

def _length_name_print(key: str) -> None:
  length_name: int = len(user_dict.get(key))
  print(f"The length of your name is {length_name}")

def _data_user_print() -> None:
  for item in item_list:
    print(msg_print_dict[item].format(user_dict.get(item)))
    if item == "name": 
      _length_name_print(item)
  
def main() -> None:
  try:
    print("Hello.")
    _set_data()
    print("######################################################")
    _data_user_print()
  except KeyboardInterrupt:
    print("\nOperation cancelled by user.")
    sys.exit(0)
  
if __name__ == "__main__":
    main()