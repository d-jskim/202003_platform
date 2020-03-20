'''
4.
다중상속을 이용하여 카드사의 클래스를 만들고
영화카드는 20% 할인
마트카드는 10% 할인
교통은 10%할인을 받는 카드 class를 구현하시오


테스트코드
<입력>
multi_card=Multi_card()
multi_card.charge(20000)
multi_card.consume(5000,'마트')
multi_card.consume(10000,'영화관')
multi_card.consume(2000,'교통')
multi_card.print()

<출력>
카드가 발급 되었습니다.
20000이 충전되었습니다.
마트에서 4500.0원을 사용했습니다.
영화관에서 8000.0원을 사용했습니다.
교통에서 1800.0원을 사용했습니다.
잔액이 5700.0원 입니다
'''


"""
    Membership_card: charge(), consume(), print()

    Movie_card(Membership_card) discount: 20%
    Mart_card(Membership_card) discount: 10%
    Transportation_card(Membership_card) discount: 10%

    Multi_card(Membership_card, Mart_card, Transportation_card)
"""

class Membership_card:

    def __init__(self):
        print("멤버십카드가 발급되었습니다.")
        self.balance = 0



    def charge(self, inputValue):
        self.balance += inputValue
        print("{}이 충전되었습니다.".format(self.balance))

    def consume(self, price, place, discount):
        discountRate = discount / 100
        if self.balance >= price:
            payment = price * (1 - discountRate)
            self.balance -= payment
            print("{}에서 {}원 사용했습니다.".format(place, payment))
        else: print("잔액이 부족합니다")
    
    def print(self):
        print("현재 잔액은 {}원입니다".format(self.balance))


class Movie_card(Membership_card):

    def consume(self, price, place):
        Membership_card.consume(self, price, place, 20)


class Mart_card(Membership_card):

    def consume(self, price, place):
        Membership_card.consume(self, price, place, 10)
    
class Transportation_card(Membership_card):

    def consume(self, price, place):
        Membership_card.consume(self, price, place, 10)

        

class Multi_card(Movie_card, Mart_card, Transportation_card):
    def __init__(self):
        print("멀티카드가 발급되었습니다.")
        self.balance = 0

    
    def consume(self, price, place):
        if place == "영화관":
            Movie_card.consume(self, price, place)
        elif place == "마트":
            Mart_card.consume(self, price, place)
        elif place == "교통":
            Transportation_card.consume(self, price, place)
        else: print("이 카드를 사용할 수 없습니다.")



multi_card=Multi_card()
multi_card.charge(20000)
multi_card.consume(5000,'마트')
multi_card.consume(10000,'영화관')
multi_card.consume(2000,'교통')
multi_card.print()

