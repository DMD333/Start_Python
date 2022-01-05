from random import randint

def rock_paper_scissors():
    arr = ['rock', 'paper', 'scissor']
    answer = True
    numar = 0

    cuvant = input('Insereaza rock, paper sau scissor: ')

    while answer is True:
        for x in range(1):
            numar = randint(0, 2)
        if cuvant == arr[numar]:
            print("It's a tie, Try again !")
        elif cuvant == 'rock' and arr[numar] == 'scissor':
            print('You won' + f'--> {cuvant} vs {arr[numar]}')
        elif cuvant == 'scissor' and arr[numar] == 'paper':
            print('You won' + f'--> {cuvant} vs {arr[numar]}')
        elif cuvant == 'paper' and arr[numar] == 'rock':
            print('You won' + f'--> {cuvant} vs {arr[numar]}')
        else:
            print('You lose')

        word = input('CONTINUE y/n ? : ')
        if word == 'y':
            cuvant = input('Insereaza rock, paper sau scissor: ')
        else:
            print('THANK YOU FOR YOUR TIME !')
            answer = False


rock_paper_scissors()


