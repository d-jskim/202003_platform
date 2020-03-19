"""14. 대문자는 소문자로, 소문자는 대문자로 출력하고
영어가 아닌 문자가 입력 되었을 때는 
'입력 형식이 잘못되었습니다' 라고 출력하는 프로그램을 작성하시오."""

inputStr = input("문자열을 입력하세요:")

def checkStr(str):
    revList = []

    if str.isalpha():
        strList = list(str)

        for char in strList:
            if char.isupper():
                revList.append(char.lower())
            else: 
                revList.append(char.upper())

        newStr = ''.join(revList)
        print(newStr)

        return

    else:
        print("입력 형식이 잘못되었습니다.")



checkStr(inputStr)