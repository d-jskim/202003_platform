"""18. 확장자가 포함된 파일 이름이 담긴 리스트에서 확장자를 제거하고
파일 이름만 추가 리스트에 저장하시오.

file = ['exit.py',hi.py','playdata.hwp',intro.jpg']

결과:
file = ['exit',hi','playdata',intro']
"""


file = ['exit.py', 'hi.py','playdata.hwp','intro.jpg']

# a function to remove file extention
def removeExt(list):
    newFile = []
    for ele in list:
        index = ele.find('.')
        #print(ele[0:index])
        newFile.append(ele[0:index])
    
    return newFile
    

print("file =", removeExt(file))



