# 딕셔너리 기본 사용법
# {키1 : 값1, 키2 : 값2, ....} 의 키와 값을 쌍으로 하는 데이터 구조

dict1 = {
  'a' : 1,
  'b' : 2,
  'c' : 3,
}

print(dict1)

# 딕셔너리는 여러 정보를 하나의 변수로 표현할 때 유용하다
student1 = {'학번' : '20260106', '이름' : '홍길동', '학과' : 'AI학과'}
print(student1)
print(student1['학과'])
student1['학과'] = '인공지능학과'
print(student1['학과'])   # 키로 값을 수정하는 것은 가능
# print(student1['몸무게'])   # 없는 key에 접근하면 에러
# 위를 get()를 이용하면 오류가 나지 않는다
print(student1.get('몸무게')) # None (해당 key가 없어도 에러나지 않음)

student1['키'] = 177  # 딕셔너리에 key : value를 추가 가능
print(student1)

student1['모바일'] = '010-1234-5678'

del(student1['키'])
print(student1)

print(student1.keys())  # student1의 모든 key 출력
print(student1.values())  # student1의 모든 value 출력

print(student1.items()) # student1의 모든 [(key, value), (key, value), ..]
