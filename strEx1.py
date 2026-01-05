a = 'Hello'
b = 'Python'
print(a + ", " + b)

print("\"평범\"의 연속은 \"비범\"이다")
print('가는 말이 고와야 \n \'오는말\'이 곱다')

# 문자열 인덱싱
a = 'Hello'
print(a[0]) # H
print(a[3]) # l

# 문자열 슬라이싱(slicing) : 부분 문자열을 얻게된다
# 변수명[시작인덱스:끝인덱스] (끝인덱스는 포함 안됨)
a = "Hello world"
print(a[1:4])   # ell
print(a[6:9])   # wor

print(a[6:])    # world (끝 인덱스를 생략하면 마지막 문자까지 모두 슬라이싱)
print(a[:5])    # Hello (시작 인덱스를 생략하면 0번째 위치부터 시작함)

# 문자열 인덱싱할 때 범위를 벗어나는 경우 오류(string index out of range) 발생
# 슬라이싱의 경우는 오류 나지 않는다

# print(a[11])    # 오류
print(a[3:11])

# 아래는 오류(파이썬에서의 문자열은 값을 변경할수 없는 불변(immutable) 객체 이기 때문)
# a[3] = 'b'
