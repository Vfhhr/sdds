import random

DESCRIPTION = 'What is the result of the expression?'

def generate_round():
    a = random.randint(1, 50)
    b = random.randint(1, 50)
    operator = random.choice(['+', '-', '*'])
    
    question = f'{a} {operator} {b}'
    
    if operator == '+':
        correct_answer = str(a + b)
    elif operator == '-':
        correct_answer = str(a - b)
    elif operator == '*':
        correct_answer = str(a * b)
    
    return question, correct_answer
