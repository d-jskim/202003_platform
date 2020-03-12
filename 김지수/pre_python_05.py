"""5. N을 입력 받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오(format 활용)"""


def mulTable(n):

    for i in range(9):
        print("{} * {} = {}".format(n, i+1, n*(i+1)))


no = int(input("구구단 출력을 원하는 단 수를 입력하시오: "))

mulTable(no)