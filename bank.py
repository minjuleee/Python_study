goalMoney = int(input("목표금액을 입력해주세요 >> "))
rate = int(input("원하는 연이자율을 입력해주세요 >> "))
money = int(input("월 납입 가능한 금액을 입력해주세요 >> "))

totalMoney = 0
month = 1
while totalMoney < goalMoney:
  totalMoney = money * month + (money * rate * 0.01 * (month * (month + 1))/(2 * 12)) * 0.846
  month += 1

print("납입 개월: ", month - 1)

