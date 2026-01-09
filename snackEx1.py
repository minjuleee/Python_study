from classEx2 import Snack

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