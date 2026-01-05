# for문의 기본 형식
# for 변수 in range(시작값, 끝값 + 1, 증감값) :
#   반복할 문장(들)

for i in range(0, 3, 1):  # i = 0, 1, 2
  print("파이썬 for문 공부중!", i)

for i in [0, 1, 2] :
  print("반복문 잼있다~!", i)
  
for i in range(2, -1, -1):
  print("얘도 3바퀴... 하지만.. 위와같이 쓰면 몇번 돌아가는지 빠르게 판단하기 곤란")

hap = 0
# 1 ~ 10까지의 합을 구하는 프로그램
for i in range(1, 11, 1):
  hap += i
  print(i, end=", ")
print(hap)

# 1 ~ 100까지의 짝수의 합
evenSum = 0
for i in range(2, 101, 2):
  evenSum += i
  # print(i, end=', ')
print("짝수 합: ", evenSum)

# 사용자에게 단을 입력받아 해당 단의 구구단을 출력하세요.
# dan = int(input("단을 입력 하세요 >>> "))
# for i in range(1, 10, 1):
#   print(f"{dan} * {i} = {dan*i}")

# 리스트를 통한 반복문
heroes = ["토르", "캡틴아메리카노", "아이언맨", "헐크", "스파이더맨"]
heroes[1] = "캡틴아메리카"
for hero in heroes :
  print(hero)
  
charactors = 'hello'
for ch in charactors:
  print(ch)