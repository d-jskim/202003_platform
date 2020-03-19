"""15. 주민등록번호를 입력하면 남자인지 여자인지 알려주는 프로그램을 작성하시오. 
(리스트 split 과 슬라이싱 활용) """


regNo = input("주민등록번호를 입력하시오: ") #string


def checkGender(regNo):
    listReg = list(regNo)
    genderNo = listReg[6:7] #genderNo is a list that has one element!
   
    if "1" in genderNo: 
        print("남자입니다.")
        return

    elif "2" in genderNo: 
        print("여자입니다.")
        return 

    else: 
        print("유효하지 않는 주민등록번호입니다.")
        return 
        
    
checkGender(regNo)
