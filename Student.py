# • 클래스명: Student
# • 속성: name, scores(정수 리스트)
# • 생성자: name, scores
# • 메서드
# • total() : 총점 반환
# • average() : 평균 반환
# • is_pass() : 평균이 60 이상이면 True, 아니면 False

import json

class Student:
  name = ''
  scores = []
  hap = 0
  avg = 0
  result = ''
  
  def __init__(self, name='', scores=[]):
    self.name += name
    self.scores += scores
  
  def total(self):
    for score in self.scores:
      self.hap += score
    return self.hap
    
  def average(self):
    self.avg = self.hap // len(self.scores)
    return self.avg
    
  def is_pass(self):
    if self.avg >= 60:
      self.result = True
    else :
      self.result = False
    return self.result
  
  def to_dict(self) :
    return {
      "name" : self.name,
      "scores" : self.scores,
      "total" : self.hap,
      "average" : self.avg,
      "is_pass" : self.result,
    }

  def to_json(self, pretty=True):
    return json.dumps(
      self.to_dict(),
      ensure_ascii=True,
      indent=2 if pretty else None
    )

student1 = Student(name="이민주", scores=[100, 70, 50, 80])
print("합계 : ", student1.total())
print("평균 : ", student1.average())
print("합격 여부 : ", student1.is_pass())

print(student1.to_json())