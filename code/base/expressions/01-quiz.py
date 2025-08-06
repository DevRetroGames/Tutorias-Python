#!/usr/bin/env python3

import sys

# Dictionary of question:answer pairs
QUESTIONS = {
    "Which planet is known as the Red Planet?": "mars",
    "What is the largest ocean in the World?": "pacificocean",
    "Who was the first Prime Minister of India?": "jawaharlalnehru",
    "What is the chemical symbol for Gold?": "au",
}

def _input_user(msg: str) -> str:
    """
    Private method to capture the user's response.

    A leading underscore indicates that a method is intended for internal use.

    Args:
        msg (str): Message displayed to the user as a prompt.
    
    Returns:
        str: The user's response, stripped of spaces and converted to lowercase.
    """
    return input(msg).replace(" ", "").lower()

def _quiz(question: str, correct_answer: str, number_question: int) -> int:
    """
    Private method to ask a question and check if the provided answer is correct.

    Uses a ternary expression for concise if-else logic.

    Args:
        question (str): The quiz question.
        correct_answer (str): The expected correct answer.
        number_question (int): The number of the question in sequence.

    Returns:
        int: Returns 1 if the answer is correct, otherwise 0.
    """
    full_question = f"Question {number_question}: {question}: "
    return int(_input_user(full_question) == correct_answer)

def main() -> None:
    """
    Main method that runs the quiz.

    ** Note **
        str is short for string  
        Args is short for arguments or parameters  
        int is short for integer  
        def is used to define a method  
            def method_name(parameters):  
                logic  
    ** Note **
    """
    print("Welcome to the GK quiz! Answer the following question")

    try:
        '''
        1. Iterate through the dictionary using `enumerate`
        2. Get the index of the question (starting from 1) and the key-value pair
        3. In each iteration, pass the parameters:
                a. key contains the question
                b. value contains the correct answer
                c. index contains the position of the key-value pair
        4. Accumulate the result in the local variable score
        '''
        score = sum(
            _quiz(question, answer, i)
            for i, (question, answer) in enumerate(QUESTIONS.items(), start=1)
        )

        # Print final score
        print(f"You scored {score}/{len(QUESTIONS)}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(0)

if __name__ == "__main__":
    """
    Entry point of the program.
    Indicates this code will only run if executed directly,
    not when imported as a module. This is a common best practice.
    """
    main()