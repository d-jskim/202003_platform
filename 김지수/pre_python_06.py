"""6. 아래와 같이 별이 찍히게 출력하시오.
숫자를 입력하세요 : 5
    ★
   ★★
  ★★★  
 ★★★★
★★★★★
 ★★★★
  ★★★
   ★★
    ★
"""

def drawDia(n):
    for i in range(n):
        print(' '*(n-(i+1)) + '★'*(i+1), end='')
        print()
    for j in reversed(range(n)):
        print(' '*(n-j) + '★'*j, end='')
        print()

no = int(input("숫자를 입력하세요: "))
drawDia(no)