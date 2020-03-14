"""3.Enter key를 눌러 주사위를 던지게 한 후, 주사위의 눈이 높은 사람이 승리하는
간단한 주사위 게임을 만드세요"""

import random

# get a number from 1 to 6
def dice():
    
    dice = [1, 2, 3, 4, 5, 6]
    return random.choice(dice)


def diceGame():

    # p1과 p2의 input값이 유효하지 않을 때 유하한 값을 얻을 때까지 반복하는 코드를 어떻게 효율적으로 쓸 수 있는지...?
    # while input != '': print("please press the enter key") -> 무한루프......
    
    input_p1 = input('Hello p1! Please, press the enter key.')
    
    if input_p1 != '':
        input_p1 = input('Please, press the enter key. This game will be started again.')
        diceGame()
    else:
        p1 = dice()

        input_p2 = input('Hello p2! Please, press the enter key.')

        if input_p2 != '':
            input_p2 = input('Please, press the enter key. This game will be started again.')
            diceGame()
        else:
            p2 = dice()

        

    

            

    print("P1's number: {}".format(p1))
    print("P2's number: {}".format(p2))

    if p1 > p2:
        print("P1 wins the round".format(p1))
        return
    elif p1 < p2:
        print("P2 wins the round".format(p2))
        return
    else:
        print("The round is a draw.")
        return



diceGame()

    

