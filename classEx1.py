class Car :
  # 자동차 객체가 가질 수 있는 속성
  color = "white"
  speed = 0
  
  # 기본생성자 : 매개변수가 없는 생성자, (self : 자기 자신의 객체를 가리키는 키워드)
  # def __init__(self):
  #   print("자동차 객체 1개 생성")
  
  def __init__(self, color, speed):
    self.color = color
    self.speed = speed
  
  # 자동차 객체가 하는 기능 -> 메서드(함수)
  def upSpeed(self, speed) :
    self.speed += speed
    print("자동차의 현재 속도 : ", self.speed)
    
  
  def downSpeed(self, speed) :
    self.speed -= speed
    print("자동차의 현재 속도 : ", self.speed)


myCar1 = Car(color="흰색", speed=60)  # Car 클래스로부터 기본생성자(매개변수가 없는 생성자 : 생략 될 수 있음)
print(myCar1.color, "속도 :", myCar1.speed)

myCar2 = Car(color="검정색", speed=30)
print(myCar2.color, "속도 :", myCar2.speed)

myCar3 = Car(color="빨간색", speed=20)
print(myCar3.color, "속도 :", myCar3.speed)

myCar1.downSpeed(30)
myCar2.upSpeed(40)

  
  