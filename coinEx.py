# 유저에게 동전 교환할 돈을 받아, 동전으로 교환할 줄때 각각의 동전을 얼마나 주면 되는지 계산하는 프로그램 작성
# 동전 : 500원짜리, 100원짜리, 50원짜리, 10원짜리
# 예 : (유저에게 입력받은 값 : 2670원)

# 0) 필요한 변수를 선언한다.
# user_money = 0, coin500 = 0, coin100 = 0, coin50 = 0, coin10 = 0
user_money, coin500, coin100, coin50, coin10 = 0, 0, 0, 0, 0

# 1) 유저에게 교환할 돈을 입력받는다
user_money = int(input("교환할 돈을 입력하세요 >> "))

# print(user_money)
# 2) 1번에서 입력한 돈을 500으로 나누어 몫을 구한다. 나머지도 구한다.
coin500 = user_money // 500
user_money %= 500
print("500원 : " + str(coin500))

# 3) 2번에서의 나머지로 100으로 나누어 몫과 나머지 구한다.
coin100 = user_money // 100
user_money %= 100
print("100원 : " + str(coin100))

# 4) 3번에서의 나머지 값으로 50으로 나눈 몫고 나머지 구한다.
coin50 = user_money // 50
user_money %= 50
print("50원 : " + str(coin50))

# 5) 3번에서의 나머지 값으로 10으로 나눈 몫고 나머지 구한다.
coin10 = user_money // 10
user_money %= 10
print("10원 : " + str(coin10))


# money = 2670
# remain = 0
# c500 = 0; c100 = 0; c50 = 0; c10 = 0

# c500 = money // 500
# remain = money % 500

# c100 = remain // 100
# remain = remain % 100

# c50 = remain // 50
# remain = remain % 50

# c10 = remain // 10
# remain = remain % 10

# print("500원짜리 동전" + str(c500) + "개, \n")
# print("100원짜리 동전" + str(c100) + "개, \n")
# print("50원짜리 동전" + str(c50) + "개, \n")
# print("10원짜리 동전" + str(c10) + "개, \n")
