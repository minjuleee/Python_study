# • 클래스명: Rectangle
# • 속성: width, height
# • 생성자: width, height
# • 메서드
# • area() : 넓이 반환
# • perimeter() : 둘레 반환
# • is_square() : 정사각형이면 True, 아니면 False

import json

class Rectangle:
  width = 0
  height = 0
  
  def __init__(self, width=0, height=0):
    self.width = width
    self.height = height
  
  def area(self):
    return self.width * self.height
  
  def perimeter(self):
    return (self.width + self.height) * 2
  
  def is_square(self):
    if self.width == self.height:
      return True
    return False
  
  def to_dict(self) :
    return {
      "width" : self.width,
      "height" : self.height,
      "area" : self.area(),
      "perimeter" : self.perimeter(),
      "is_square" : self.is_square(),
    }

  def to_json(self, pretty=True):
    return json.dumps(
      self.to_dict(),
      ensure_ascii=True,
      indent=2 if pretty else None
    )
  
rect1 = Rectangle(width=20, height=80)
print("넓이 : ", rect1.area())
print("둘레 : ", rect1.perimeter())
print("정사각형 여부 : ", rect1.is_square())

print(rect1.to_json())
    