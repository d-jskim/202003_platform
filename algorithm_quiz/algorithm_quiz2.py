'''
2.
첫 번째 숫자를 두 번째 숫자부터 마지막 숫자까지 차례대로 비교하여
가장 작은 값을 찾아 첫 번째에 놓고,  두번째 숫자를 세 번째 숫자부터
마지막 숫자까지 차례대로 비교하여그 중 가장 작은 값을 찾아
두 번째 위치에 놓는 과정을 반복하며 정렬하는것을 선택정렬이라고 합니다.
주어진 리스트를 선택정렬함수(select_sort)를 생성하여 오름차순으로 정렬하시오
list=[6,2,3,7,8,10,21,1]

<입력>
print(select_sort(list))

<출력>
[1, 2, 3, 6, 7, 8, 10, 21]

'''

list=[6,2,3,7,8,10,21,1]

def findMin(list):
    min = list[0]
    minIndex = 0

    for i in range(1, len(list)):
        if list[i] < min:
            min = list[i]
            minIndex = i
    
    return minIndex

def select_sort(list):
    newList = []

    for i in range(len(list)):
        minIndex = findMin(list)
        newList.append(list[minIndex])
        list.pop(minIndex)
    
    return newList

print(select_sort(list))

