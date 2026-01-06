# while 조건식:
  # 반복 수행될 명령문(들)
 
 
# 숫자를 입력받아 1부터 그 숫자까지의 합을 구하는 프로그램 작성
# num = int(input("숫자 입력 >> "))
# i = 1
# sum = 0
# while i <= num:
#   sum += i
#   i+=1
  
# print("합계 : ", sum)

# 구구단 출력
dan = 1
while dan <= 9:
  i = 1
  while i <= 9:
    print(f"{dan} x {i} = {dan * i}")
    i+=1
  print("")
  dan += 1
  
while True:
  print("ㅋ", end=" ")