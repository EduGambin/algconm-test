#!/usr/bin/env python

import random
import csv


# Read the questions from the "questions.csv" file using the csv module
def read_questions():
    with open('questions.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row
        questions = list(reader)
    return questions


correct_answers = 0
failed_answers = []
questions = read_questions()


# The CSV contains a list of questions and answers in the following format:
# question,answer,fake1,fake2,fake3

def main():
    global correct_answers
    global failed_answers
    global questions

    print("-" * 80)
    print("Elige una opción:")
    print("  1. 10 preguntas aleatorias")
    print("  2. 20 preguntas aleatorias")
    print("  3. 30 preguntas aleatorias")
    print("  4. Todas las preguntas")
    print("  5. Salir")
    print()

    while True:
        try:
            option = int(input("Opción: "))
            if option < 1 or option > 5:
                raise ValueError
            break
        except ValueError:
            print('\033[1;31mIntroduce un número entre 1 y 5.\033[0m')

    if option == 1:
        num_questions = 10
    elif option == 2:
        num_questions = 20
    elif option == 3:
        num_questions = 30
    elif option == 4:
        num_questions = len(questions)
    else:
        exit()

    print("Seleccionadas {} preguntas".format(num_questions))
    print("-" * 80)

    # Shuffle the questions
    random.shuffle(questions)

    questions = questions[:num_questions]

    for j, q in enumerate(questions):
        # Make room
        print()

        # Print the question in blue and bold
        print('\033[1;34m{}. {}\033[0m'.format(j + 1, q[0]))

        # Shuffle the answers but remember the correct answer
        answers = [q[1], q[2], q[3], q[4]]
        random.shuffle(answers)

        correct_answer = answers.index(q[1])

        # Print the answers
        for i, a in enumerate(answers):
            print('  {}. {}'.format(i + 1, a))
        print()

        # Get the user's answer. If it's not a number or it's not between 1 and
        # 4, ask again
        while True:
            try:
                user_answer = int(input('Respuesta: '))
                if user_answer < 1 or user_answer > 4:
                    raise ValueError
                break
            except ValueError:
                print('Por favor, introduce un número entre 1 y 4.')

        if user_answer == correct_answer + 1:
            print('\033[1;32m¡Correcto!\033[0m')
            correct_answers += 1
        else:
            print('\033[1;31m¡Incorrecto!\033[0m')
            print('La respuesta correcta es la {}.'.format(correct_answer + 1))
            failed_answers.append(j+1)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Terminado por el usuario.')

    print()
    print('Has acertado {} preguntas de {}.'.format(
        correct_answers, len(questions)))
    if failed_answers:
        print('Preguntas falladas: {}'.format(
            ', '.join(map(str, failed_answers))))
