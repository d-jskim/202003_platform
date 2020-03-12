"""3.Enter key를 눌러 주사위를 던지게 한 후, 주사위의 눈이 높은 사람이 승리하는
간단한 주사위 게임을 만드세요"""

import random

def diceGame():
    
    dice = [1, 2, 3, 4, 5, 6]
    return random.choice(dice)


Jane = diceGame()
Mike = diceGame()
print("Jane's number: ", Jane)
print("Mike's number: ", Mike)


if Jane > Mike: 
    print("Result: Jane wins.")

elif Jane < Mike:
    print("Result: Mike wins.")
    
else:
    print("Result: The game ended in a draw.")
