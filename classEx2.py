# Snack (과자) 객체를 만든다.
# Snack은 productName, weight, price라는 속성을 가지고 있다.
# Snack은 displayInfo() 메서드를 가지고 있고, displayInfo 메서드를 호출하면
# 상품명, 중량, 가격이 출력된다.

class Snack:
  productName = ''
  weight = 0.0
  price = 0
  cnt = 0   # 과자의 총 갯수(클래스 변수: 모든 객체가 공유하는 변수)
  qty = 0   
  
  # 생성자의 역할 : 멤버 변수(필드)의 값을 초기화
  def __init__(self, productName = "", weight = 0.0, price = 0):
    self.productName = productName
    self.weight = weight
    self.price = price
    Snack.cnt += 1
  
  def displayInfo(self) :
    print(f"상품명 : {self.productName}, 중량 : {self.weight}, 가격 : {self.price}, 과자개수 : {Snack.cnt}")

