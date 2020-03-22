'''
4.
탐욕 알고리즘은 최적해를 구하는 상황에서 사용하는 방법입니다.
여러 경우 중 하나를 선택할 때 그것이 그상황에서 가장 좋다고 생각하는 것을
선택해 나가는 방식으로 진행하여 답을 구합니다.
하지만 탐욕알고리즘은 그 상황에서 가장 좋다고 생각하는 것을 선택해 나가는
방식이기 때문에 가장 좋은 결과를 얻는 것이 보장되는것은 아닙니다.
탐욕 알고리즘을 이용하여 동전을 지불하는 함수(greedy)를 짜는데 지불해야 하는
동전의 갯수가 최소가 되도록 함수를 구현하시오
(input 으로 액수와 동전의 종류를 입력하게 구현)

<입력>
print(greedy())

<출력>
액수입력 :  1050
동전의 종류 :  100 50 10
100원 동전 10개, 50원 동전 1개, 10원 동전 0개
'''

def bubble_sort_asc(list):

    for length in range(len(list), 0, -1):
        for j in range(length-1):
            if list[j] < list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    
    return list
    

def greedy():
    
    price = int(input("액수를 입력하시오:"))
    coinType = input("동전의 종류를 입력하시오(예시: 100 50 10):")

    tempList = coinType.split() # string을 공백 기준으로 split
    intList = list(map(int, tempList)) # 숫자 형변환: string to int

    coinList = bubble_sort_asc(intList) # 오름차순으로 정렬

    noCoinList = [] 
    dividend = price

    for i in range(len(coinList)):
        noCoinList.append(dividend // coinList[i])
        dividend = dividend % coinList[i]
        
    index = 0
    while index < len(noCoinList):
        print("{}원 동전 {}".format(coinList[index], noCoinList[index]), end='')
        print(", ", end='')
        index += 1

    # "0, None"을 없애는 방법........? 


print(greedy())





