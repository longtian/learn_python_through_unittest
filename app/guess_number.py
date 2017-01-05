import random

number = random.randint(0, 100)

random.seed(77)


def loop():
    guess = int(input(u'输入'))
    if guess < number:
        print('bigger')
        return False
    else:
        if guess == number:
            print('bingo')
            return True
        else:
            print('smaller')
            return False


while not loop():
    print('', end='')
