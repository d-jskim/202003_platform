"""11. 최대공약수를 구하는 함수를 구현하시오"""

# prime numbers: 소수
primeNumbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# a function for finding the Greatest Common Factor
def findGCF(a, b):
    
    # a list for common factors
    commonFactors = []

    for i in range(len(primeNumbers)): 
        divisor = primeNumbers[i]

        while a % divisor == 0 and b % divisor == 0: 
            a = a // divisor
            b = b // divisor
            commonFactors.append(divisor)

    #print(commonFactors)

    result = 1 #initialization before for loop
    for j in range(len(commonFactors)):
        result *= commonFactors[j]

    
    return result
        

input1 = int(input("2이상의 양수를 입력하시오: "))
input2 = int(input("2이상의 양수를 한 번 더 입력하시오:"))
resGCF = findGCF(input1, input2)
print("{}와(과) {}의 최대공약수: {}".format(input1, input2, resGCF))


        


