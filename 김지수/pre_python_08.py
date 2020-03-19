"""8. 정수를 입력했을 때 짝수인지 홀수인지 핀별하는 코드를 작성하시오"""


def oddAndEven(no):

    if no % 2 == 0:
        print("{}은(는) {}입니다.".format(no, "짝수"))
    
    else:
        print("{}은(는) {}입니다.".format(no, "홀수"))

inputNo = int(input("정수를 입력하시오: "))
oddAndEven(inputNo)