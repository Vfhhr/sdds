import random

def main():
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    
    for _ in range(3):
        a = random.randint(1, 50)
        b = random.randint(1, 50)
        operator = random.choice(['+', '-', '*'])
        
        question = f'{a} {operator} {b}'
        print(f'Question: {question}')
        
        if operator == '+':
            correct_answer = str(a + b)
        elif operator == '-':
            correct_answer = str(a - b)
        elif operator == '*':
            correct_answer = str(a * b)
        
        user_answer = input('Your answer: ')
        
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    
    print(f'Congratulations, {name}!')

if __name__ == '__main__':
    main()
