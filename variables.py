# 변수 : 메모리 영역(RAM)에 저장되어 있는 값.
# 저장되지 않은 값은 언젠가 소멸된다.

student_name = "홍길동"
# print(student_name)

student_name = "둘리"
print(student_name)

a = 5
b = 3
temp = a
a = b
b = temp

print("a = ", a)
print("b = ", b) 

# 파이썬에서의 기본 데이터 타입(데이터의 종류)
boolVar = True    # boolean 타입 (참(True) 또는 거짓(False))
boolVar2 = False
intVar =  100      # int 타입 : 정수
floatVar = 3.145  # float 타입 : 실수
strVar = "True"   # 문자열 타입 : 문자열

print(type(boolVar))
print(type(boolVar2))
print(type(intVar))
print(type(floatVar))
print(type(strVar))

str1 = '파이썬은 재밌네'

print(str1)

str2 = """파이썬은 재밌네"""
print(str2)
