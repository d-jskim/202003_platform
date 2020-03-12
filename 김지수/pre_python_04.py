"""4. 삼각형의 가로와 높이를 받아서 넓이를 출력하는 함수를 작성하시오."""

def triangleArea(b, h):
    area = (b*h) / 2
    return area


base = int(input("밑변의 길이를 정수로 입력하시오: "))
height = int(input("높이를 정수로 입력하시오: "))


print("삼각형의 넓이: ", triangleArea(base, height))





