"""
9. 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다.
점수를 입력했을 때 해당 학점이 출력되도록 하시오.
81~100 : A
61~80 : B
41~60 : C
21~40 : D
0~20 : F
"""



def grade(score):

    if score >= 81 and score <=100:
        print("A")
        return
    elif score >= 61 and score <=80:
        print("B")
        return
    elif score >= 41 and score <=60:
        print("C")
        return
    elif score >= 21 and score <=40:
        print("D")
        return
    else:
        print("F")
        return

inputScore = float(input("점수를 입력하시오: "))

grade(inputScore)