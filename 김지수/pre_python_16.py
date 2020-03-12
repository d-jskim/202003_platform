"""16. 1부터 50 까지의 숫자 중에서 3의 배수를 공백으로 구분하여 출력하시오."""



def multiplesOfThree():

    list = []

    for i in range(50):
        number = i + 1
        if number % 3 == 0:
            list.append(str(number)) #parseStr for using str.join()
    
    return list

listRes = multiplesOfThree()


print(" ".join(listRes))


            
