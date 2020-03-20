'''
2.
년, 월, 일을 입력하면 그 날이 무슨 요일인지 출력하는 함수를 만드세요.


테스트코드
<입력>
print("%d년 %d월 %d일은 %s 입니다." % (myYear, myMonth, myDay, printDayOfTheWeek(myYear, myMonth, myDay)))

<출력>
연도를 입력하시오 : 2020
월을 입력하시오 : 3
일을 입력하시오 : 13
2020년 3월 13일은 금요일 입니다.

'''

"""
date.weekday()
정수로 요일을 반환합니다. 월요일은 0이고 일요일은 6입니다. 예를 들어, date(2002, 12, 4).weekday() == 2, 수요일. 
"""

from datetime import date

myYear = int(input("연도를 입력하시오"))
myMonth = int(input("월을 입력하시오"))
myDay = int(input("일을 입력하시오"))

# 요일 출력
def printDayOfTheWeek(myYear, myMonth, myDay):

    weekdays = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
    weekday = weekdays[date(myYear, myMonth, myDay).weekday()]
    return weekday


print("%d년 %d월 %d일은 %s 입니다." % (myYear, myMonth, myDay, printDayOfTheWeek(myYear, myMonth, myDay)))