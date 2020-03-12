"""17. 1988년 ~ 2060년까지 중 월드컵이 개최되는 연도를 출력하시오"""


# 2002 World Cup was held in S.Korea
def yrs_WorldCup():
    before2002 = []
    after2002 = []

    for year in range(2002, 1988, -4):
        before2002.append(year)
   
    for year in range(2002 + 4, 2060, +4):
        after2002.append(year)

    before2002.reverse()

    yearsOfWC = before2002 + after2002
    print(yearsOfWC)

 
yrs_WorldCup()