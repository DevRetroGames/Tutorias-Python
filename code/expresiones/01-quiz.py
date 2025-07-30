#!/usr/bin/env python3

def _input_user(msg):
    """
    Método privado para capturar el ingreso de la respuesta del usuario.
    
    Para señalar que un método es privado, se antepone un guion bajo.

    Args:
        msg: Mensaje que se muestra al usuario para solicitar la respuesta.
    Return:
        str: Se devuelve la respuesta del usuario, sin espacios y en minusculas.
    """
    return input(msg).replace(" ", "").lower()

def _quiz(question, correct_answer, number_question):
    """
    Método privado para realizar la pregunta al usuario y comprobar si la respuesta estregada es correcta.

    Se utiliza ternaria, una forma simple y elegante de tipico if-else.

    Args:
        question: contiene la pregunta.
        correct_answer: contiene la respuesta correcta.
        number_question: contiene el número de la pregunta.
    Return:
        int: si la respuesta es correcta, devolver 1, de lo contrario, devolver 0.
    """
    full_question = f"Question {number_question}: {question}: "
    return 1 if _input_user(full_question) == correct_answer else 0

def main():
    """
    Método principal

    ** Nota **
        str es la abreviatura de string
        Args es la abreviatura de Argumentos o parametros
        int es la abreviatura de integer o entero
        def sirve para construir un método.
            def nombre_metodo(parametros):
                logica
    ** Nota **
    """
    msg = "Welcome to the GK quiz! Answer the following question"
    print(msg)

    # diccionario de clave : valor
    questions = {
        "Which planet is known as the Red Planet?": "mars",
        "What is the largest ocean in the World?": "pacificocean",
        "Who was the first Prime Minister of India?": "jawaharlalnehru",
        "What is the chemical symbol for Gold?": "au",
    }

    # variable local acumulativa
    score = 0

    '''
    1.- Recorre el diccionario usando `enumerate`
    2.- Obtener el índice de la pregunta (empezando en 1) y el par clave:valor
    3.- En cada iteración, pasar los parametros:
            a.- clave contiene la pregunta
            b.- valor contiene la respuesta
            c.- indice contiene la posicion de clave:valor
    4.- Acumular el resultado en la variable local score
    '''
    for i, (question, answer) in enumerate(questions.items(), start=1):
        score += _quiz(question, answer, i)

    # imprimir resultado
    print(f"You scored {score}/4")

if __name__ == "__main__":
    """
    Punto de entrada del programa
    Indica que solo se ejecutara si se corre de forma directa y no como un import o llamado desde otro archivo.
    Es una practica común.
    """
    main()