"""10. 팩토리얼을 구하는 함수를 작성하시오.
ex ) 5! = 5x4x3x2x1
  print(factoral(5)) -> 120 출력"""


def factorial(no):

    #initialization for multiplication
    result = 1

    for i in reversed(range(no)):
        number = i + 1
        result *= number

    #return the result of factorial cal  
    return result


inputNo = int(input("정수를 입력하시오: "))
factorialRes = factorial(inputNo)

print("factorial({}) -> {}".format(inputNo, factorialRes))