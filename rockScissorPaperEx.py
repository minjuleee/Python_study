# 유저와 컴퓨터가 가위바위보 게임을 한다
# 가위 = 1, 바위 = 2, 보 = 3이라고 할때
# 컴퓨터가 랜덤하게 가위바위보 중 하나를 내고
# 유저도 1, 2, 3 번 중 하나를 입력 받는다.
#
# 유저가 이겼으면 "이겼다", 졌으면 "졌다", 비겼으면 "비겼다"라고 출력하는 프로그램을
# 작성하세요.
# 
import random

user = int(input("가위바위보 중 하나를 내세요. *가위 = 1, 바위 = 2, 보 = 3 >> "))
com = random.randint(1, 3)
print(user, com)

result = ''
# 결과 판정
if user == com :
  result = '비겼다'
elif (user == 1 and com == 3) or (user == 2 and com == 1) or (user == 3 and com == 2 ) :
  result = '이겼다'
else : 
  result = '졌다'
  
# f스트링을 이용하여 편하게 출력해 보자
print(f"유저는 {user}, 컴퓨터는 {com}, 결과는 {result}")


# user = int(input("가위 바위 보를 입력해주세요(가위 = 1, 바위 = 2, 보 = 3) >> "))
# computer = random.randrange(1, 4)
# # computer = random.randint(1, 3)
# # print(computer)

# if computer > user :
#   if computer == 3 and user == 1:
#     print("게임에서 승리하였습니다 컴퓨터: 보, 유저: 가위")
#   else:
#     print("게임에서 졌습니다 컴퓨터: ", computer, "유저: ", user)
  
# elif computer < user :
#   if computer == 1 and user == 3:
#     print("게임에서 패배하였습니다 컴퓨터: 가위, 유저: 보")
#   else:
#     print("게임에서 승리하습니다 컴퓨터: ", computer , "유저: ", user)

# else : 
#   print("게임에서 비겼습니다")

