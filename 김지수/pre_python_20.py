"""20. 1부터 100까지 369 게임을 하려고 한다.
3,6,9가 들어가는 부분에는 '짝' 을 출력하고, 
5의 배수에는 '아자' 를 출력,
그외에는 수를 출력하는 프로그램을 만드시오."""

def game369():
    
    gameList = []
    numList = []

    for i in range(100):
        number = i + 1
        
        numStr = str(number)
        numList = list(numStr)

        if "3" in numList:
            gameList.append("짝")
        elif "6" in numList:
            gameList.append("짝")
        elif "9" in numList:
            gameList.append("짝")
        elif number % 5 == 0 :
            gameList.append("아자")
        else: 
            gameList.append(numStr);
        
    return gameList

print(game369())
            


       