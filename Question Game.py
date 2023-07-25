def newGame():
    guesses = []
    correct_answer = 0
    question_number = 1

    for key in questions:
        print()
        print(key)
        for i in choices[question_number - 1]:
            print(i)
        print()
        guess = input("Enter your Choice (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_answer += checkAnswer(questions.get(key),guess)
        question_number += 1
    displayScore(correct_answer,guesses)
def checkAnswer(answer,guess):
    if answer == guess:
        return 1
    else:
        return 0
def displayScore(correct_answer, guesses):
    print('------------------------------------')
    print('Result')
    print('------------------------------------')
    print('Answer: ', end=' ')
    for i in questions:
        print(questions.get(i), end=' ')
    print()
    print('Gueses: ', end=' ')
    for i in guesses:
        print(i, end=' ')
    print()

    score = int((correct_answer/len(questions)) * 100)
    print('Your Total score is: '+ str(score) + '%')

questions ={'What is the capital city of France?: ': 'B',
            'What is the chemical symbol for water?: ': 'B',
            'Who was the first President of the United States?: ': 'B',
            'Which country is known as the Land of the Rising Sun?: ': 'B',
            'Who wrote the play Romeo and Juliet?: ': 'A',
            'In which sport would you perform a slam dunk?: ': 'B',
            'Which movie features a character named Luke Skywalker?: ': 'A',
            'Who is known as the King of Pop?: ': 'A',
            'What is the largest land animal in the world?: ': 'A',
            'Who co-founded Apple Inc. along with Steve Jobs and Ronald Wayne?:': 'C'}

choices = [['A) London' ' B) Paris' ' C) Berlin' ' D) Rome'],
           ['A) Wa' ' B) H2O' ' C) W' ' D) H2'],
           ['A) Thomas Jefferson' ' B) George Washington' ' C) Abraham Lincoln' ' D) Benjamin Franklin'],
           ['A) China' ' B) Japan' ' C) South Korea' ' D) Vietnam'],
           ['A) William Shakespeare' ' B) Jane Austen' ' C) Mark Twain' ' D) Charles Dickens'],
           ['A) Soccer' ' B) Basketball' ' C) Tennis' ' D) Baseball'],
           ['A) Star Wars' ' B) The Lord of the Rings' ' C) Harry Potter' ' D) The Matrix'],
           ['A) Michael Jackson' ' B) Elvis Presley' ' C) Madonna' ' D) Prince'],
           ['A) African Elephant' ' B) Polar Bear' ' C) Giraffe' ' D) Lion'],
           ['A) Bill Gates' ' B) Jeff Bezos' ' C) Steve Wozniak' ' D) Larry Page']]

newGame()