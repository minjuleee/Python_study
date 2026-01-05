# 중첩 if문 예제

x = int(input("x값 입력 >>> "))
y = int(input("y값 입력 >>> "))

if x == y :
  print("x와 y가 같습니다.", x , y)
else :
  if x < y :
    print("x가 y보다 작습니다. ", x, y)
  else :
    print("x가 y보다 큽니다. ", x, y)

print("프로그램 종료")