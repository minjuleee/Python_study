class Car :
  # 자동차 객체가 가질 수 있는 속성
  color = "white"
  speed = 0
  
  # 자동차 객체가 하는 기능 -> 메서드(함수)
  def upSpeed(speed) :
    print("자동차의 현재 속도 : ", speed)
  
  def downSpeed(speed) :
    print("자동차의 현재 속도 : ", speed)


myCar1 = Car()  # Car 클래스로부터 기본생성자(매개변수가 없는 생성자 : 생략 될 수 있음)
print(myCar1)
  
  