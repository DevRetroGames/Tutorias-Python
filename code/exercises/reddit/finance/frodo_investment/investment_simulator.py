#!/usr/bin/env python3

import re
from math import floor

class InvestmentSimulator:
    ANNUAL_RATE = 0.045  # Annual interest rate: 4.5%
    DAYS_PER_MONTH = 30  # Approximate number of days in a month

    def __init__(self, messages: dict):
        # Initialize investment parameters and localized messages
        self.amount = 0.0
        self.days = 0
        self.final_amount = 0.0
        self.monthly_profit = 0.0
        self.months = 0
        self.messages = messages

    @staticmethod
    # This method does not depend on instance variables. It can be called without creating an object.
    # It's used here to validate user input using a regular expression.
    def _is_valid_regex(input_str: str, pattern: str) -> bool:
        # Check if the input string matches the given regex pattern
        return re.fullmatch(pattern, input_str.strip()) is not None

    def _get_user_input(self, prompt: str, pattern: str) -> str:
        # Prompt user for input and validate it against the regex pattern
        while True:
            user_input = input(prompt).strip()
            if self._is_valid_regex(user_input, pattern):
                return user_input
            print(self.messages["messages"]["invalid_input"])

    def _ask_amount(self):
        # Ask user how much money to invest
        while True:
            amount_str = self._get_user_input(self.messages["prompts"]["ask_amount"], r"\d+(\.\d+)?")
            amount = float(amount_str)
            if amount > 0:
                self.amount = amount
                break
            print(self.messages["messages"]["amount_must_be_positive"])

    def _ask_days(self):
        # Ask user for how many days they want to invest
        while True:
            days_str = self._get_user_input(self.messages["prompts"]["ask_days"], r"\d+")
            days = int(days_str)
            if days > 0:
                self.days = days
                break
            print(self.messages["messages"]["days_must_be_positive"])

    def _calculate_compound_interest(self):
        # Calculate compound interest based on the provided investment duration
        self.months = floor(self.days / self.DAYS_PER_MONTH)
        monthly_rate = self.ANNUAL_RATE / 12

        self.final_amount = self.amount * ((1 + monthly_rate) ** self.months)
        total_profit = self.final_amount - self.amount
        self.monthly_profit = total_profit / self.months if self.months > 0 else 0

        # Round results for better presentation
        self.final_amount = round(self.final_amount, 2)
        self.monthly_profit = round(self.monthly_profit, 2)

    def _display_results(self):
        # Print the summary of the investment results
        print(self.messages["messages"]["investment_summary"])
        print(self.messages["messages"]["initial_amount"].format(self.amount))
        print(self.messages["messages"]["days_invested"].format(self.days))
        print(self.messages["messages"]["months_counted"].format(self.months))
        print(self.messages["messages"]["profit_per_month"].format(self.monthly_profit))
        print(self.messages["messages"]["total_amount"].format(self.final_amount))

    def run(self):
        # Main execution flow: gather input, calculate interest, display results
        self._ask_amount()
        self._ask_days()
        self._calculate_compound_interest()
        self._display_results()