"""7. 1부터 100까지 수의 합을 계산하고 있다. 
이 때 합이 최초로 1000을 넘게 하는 수가 무엇인지 코드를 만들고 답을 구하시오"""




def sum():

    #sum 변수 선언 & 0으로 초기화
    sum = 0 

    #1부터 100까지 합 -> range(100) 100번의 for loop
    for i in range(100):
        number = i + 1 #1부터 시작
        sum += number 
        
        if sum > 1000: 
            return number

result = sum()
print("합이 최초로 1000을 넘게 하는 수: ", result)
