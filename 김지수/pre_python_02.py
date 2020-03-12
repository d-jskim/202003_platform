""""2.if문을 이용해 첫번째와 두번째 수, 연산기호를 입력하게 하여 계산값이 나오는 계산기를 만드시오"""

input1 = float(input("숫자를 입력하시오: "))
inputOp = input("연산자를 입력하시요(+, -, *, /): ")
input2 = float(input("숫자를 한 번 더 입력하시오: "))

# calculation
def cal(operator, a, b):

    if operator == "+":
        return a + b
    
    elif operator == "-":
        return a - b

    elif operator == "*":
        return a * b
    
    elif operator =="/":
        return a / b
    else:
        print("계산할 수 없습니다. '+', '-', '*', '/' 중 하나만 선택해주세요.")
        return 

print("연산 결과: ", cal(inputOp, input1, input2))