# 파이썬 연산자 종류

# 1. 산술 연산자
# 

a = 4; b = 3
print(a+b, a-b, a*b, a/b, a//b, a*b, a**b)

# 문자열끼리의 덧셈은 문자열이 연결된다.
name = '홍길동'
job = '은 학생입니다'

print(name + job)

# 산술연산자에서 ()를 이용하여 우선순위를 정할 수 있다.
print((3-2) * 4 + 5 / 12)

# 2. 대입 연산자
x = 3
x += 3    # x = x + 3
print(x)

x *= 2  # x = x * 2
print(x)

x -= 5  # x = x - 5
print(x)

x /= 7  # x = x / 7
print(x)


# 3. 관계연산자 : (비교 연산자) - 결과값이 참 (True) 또는 거짓 (False)로 나오는 연산자. 조건문이나 반복문에서 사용된다.

a, b = 100, 200
print(a == b, a != b, a > b, a <= b ) # F, T, F, T
print(a > 5)  # T

str1 = "hello"
str2 = "Hello"

print(str1 != str2) # T

str3 = "홍길동"
str4 = "홍 길동"

print(str3 != str4) # T

# 논리 연산자 : 2개 이상의 비교연산식을 하나로 묶어 하나의 참 / 거짓 결과를 얻을 때 사용
a, b = 100, 200

print(a > 5 and b > 300)  # F
print(b >= 100 and not(a < 200))  # F


