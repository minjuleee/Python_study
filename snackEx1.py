from classEx2 import Snack
import json

# mySnack1 = Snack(productName=input("상품명 : "), weight=input("중량 : "), price=input("가격 : "))
# mySnack1.displayInfo()
# nutrition = {"나트륨":"200mg", "탄수화물": "18g"}
snack1 = Snack(productName="포카칩", weight= 60.0, price=1900
               , nutrition={"나트륨" : "20g", "탄수화물" : "18g"})
snack1.displayInfo()

snack2 = Snack(productName="감자깡", weight= 40.0, price=1200)
snack2.displayInfo()

snacks = []
snacks.append(snack1)
snacks.append(snack2)

for s in  snacks:
  s.displayInfo()
  print(s.to_dict())

print(snack1.to_json())   # snack1 객체를 json 표현
print(snack2.to_json())   # snack2 객체를 json 표현

# snack1, snack2를 리스트 묶어서 모든 과자객체를 하나의 json으로 표현
print(json.dumps(
  [s.to_dict() for s in snacks],
  ensure_ascii=True,
))


