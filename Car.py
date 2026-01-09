# • 클래스명: Car
# • 속성: model(모델명), fuel(연료량)
# • 생성자: model, fuel(기본값 0)
# • 메서드
# • refuel(amount) : 연료량 증가
# • drive(distance) : distance만큼 주행 시도
# • 규칙: 1km 주행에 연료 1 소모
# • 연료가 부족하면 주행하지 않기
# • status() : 현재 모델명과 연료량을 문자열로 반환

import json

class Car:
  model = ''
  fuel = 0
  
  def __init__(self, model='', fuel=0):
    self.model = model
    self.fuel = fuel
  
  def refuel(self, amount):
    self.fuel += amount
    
  def drive(self, distance):
    if self.fuel >= distance:
      self.fuel -= distance 
    else:
      print("연료가 부족해 주행 x")
    
  def status(self):
    print(f"모델명 : {self.model}, 연료량 : {self.fuel}")
  
  def to_dict(self) :
    return {
      "model" : self.model,
      "fuel" : self.fuel,
    }

  def to_json(self, pretty=True):
    return json.dumps(
      self.to_dict(),
      ensure_ascii=True,
      indent=2 if pretty else None
    )
  
car1 = Car(model="BMW", fuel=500)
car1.status()

car1.refuel(500)
car1.status()

car1.drive(1500)
car1.status()

print(car1.to_json())
  
    
    
  