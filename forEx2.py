# 중첩 for 문 : for문 안에 또 다른 for 반복문이 있는 구조
# 바깥의 for문 1회전에 대해 안쪽의 for문이 반복되는 구조이다.
# 총 실행 횟수는 : 바깥쪽 for문의 실행횟수 * 안쪽 for문의 실행횟수

for i in range(3) :   # i = 0, 1, 2
  print("☆", end=" ")
  for j in range(2) :   # j = 0, 1
    print("★", end=" ")
print("")

# 구구단 전체를 출력하는 프로그램 작성
for dan in range(2, 10, 1):
  for i in range(1, 10, 1):
    print(f"{dan} * {i} = {dan*i}", end=" ")
  print("")
# for i in range(9) :
#   for j in range(9) :
#     print(f"{(i+1)} x {(j+1)} = {(i+1) * (j+1)}")