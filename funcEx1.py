# 사용자 정의 함수 연습 (함수 만들기, 호출 연습)
def sayHello(userName, age) :
  print(f"{userName}님 안녕하세요", age)
  age = age + 1
  return age
  
# userName = input('이름 입력 >> ')
# age = 20
# age = sayHello(userName, age)
# print(age)

# 두 개의 정수를 입력받아 각각 덧셈, 뺄셈, 나눗셈 곱셈 하는 함수로 결과를 만들어 출력
def add(a, b) :
  return a + b
  
def sub(a, b) :
  if a < b :
    return b - a
  return a - b
  
def div(a, b) :
  if b == 0:
    print('0으로 나눌 수 없습니다')
  else :
    return a / b
  
def mul(a, b) :
  return a * b

# a를 b번 곱하는 함수
def myExam(a, b) :
  result = 1
  for i in range(b):
    result *= a
  return result

def mySum(list):
  print(list)
  list[0] = 10
  return list
  
a = int(input("a 입력 : "))
b = int(input("b 입력 : "))
cal = input("연산자 : ")

if cal == '+':
  print("두 수의 합: ", add(a, b))
elif cal == '-':
  print("두 수의 차: ", sub(a, b))    
elif cal == '/':
  print("두 수의 나눗셈: ", div(a, b))
elif cal == '*':
  print("두 수의 곱: ", mul(a, b))
elif cal == '**':
  print("두 수의 제곱: ", myExam(a, b))
else:
  print("해당 문자는 연산을 지원하지 않습니다")

list = [1, 2, 3, 4, 10]
print(mySum(list))


