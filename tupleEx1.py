# tuple 기본 숙지

tt1 = (10, 20, 30)
tt2 = 1, 2, 3
print(tt1, tt2)

tt3 = (10)  # 튜플로 만들어지지 않음. 튜플로 만들려면 tt3 = (10, )
print(tt3)  # 튜플의 원소가 1개라도 콤마를 찍지 않으면 튜플로 생성되지 않는다. 주의!

print(tt1[0])
# tt1[0] = 100  튜플은 값 수정이 되지 않는다.
# tt1.append()

# del(튜플명) : 튜플 삭제
del(tt2)

tt3 = (1, 2, 3, 4, 5)
print(tt3[0:3])

list_tt3 = list(tt3)  # 튜플을 리스트로 변환
print(list_tt3) 

tuple3 = tuple(list_tt3)  # 리스트를 튜플로 변환
print(tuple3)

tt4 = (4, 6)
a, b = tt4
print(a, b)


