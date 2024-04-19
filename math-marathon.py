# Timed Math Challenge
# This program generates random math questions and measures the time it takes to answer them,
# providing the score of the results.

import time
import random

score = 0  # Initialize score counter

t = 60  # Time limit in seconds
start_time = time.time()  # Start time of the game

# Dictionary of arithmetic operations
operator_functions = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b
}

operators = ["+", "-", "*"]


def Mathgenerator():
    # Generates a random math question and evaluates the user's answer.
    number1 = random.randint(0, 10)
    number2 = random.randint(0, 10)
    picked_operator = random.choice(operators)

    awnser = input("{num1} {operator} {num2} = ".format(operator=picked_operator, num1=number1, num2=number2))

    try:
        awnser = int(awnser)
    except:
        awnser = 0

    if awnser == operator_functions[picked_operator](number1, number2):
        print("Correct!")
        return 1
    else:
        print("Incorrect!")
        return 0

print("This is a math marathon!")
print("You will have 1 minute to answer as many questions as you can.")
print()

if input("Are you ready? ").lower() not in ["yes", "y", "yee", "yeah"]:
    print()
    print("I guess this is too hard for you...")
    print("See you next time!")
    quit()

# Main game loop
while time.time() - start_time < t:
    score += Mathgenerator()

# Display final score
print("You finished the game with a score of {}".format(score))