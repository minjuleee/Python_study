# 리스트 기본 문법

aa = []   # 빈 리스트 생성
print(aa)

for i in range(0, 100):
  aa.append(i)

print(aa)
print(len(aa))

list1 = ["apple", "banana", "grape", "watermelon"]
for fruit in list1 :
  print(fruit)
  
  
# 1 ~ 100까지의 랜덤한 수 10개를 list2라는 리스트에 저장하세요
import random

list2 = []
for i in range(10):
  list2.append(random.randrange(1, 101)) 
print(list2)

# 리스트
dd = [10, 20, '파이썬', 3.14, False, None]
print(dd)   # 파이썬의 리스트에는 다양한 데이터 타입을 저장할 수 있다 

# 인덱싱
print(dd[2])
print(dd[-2])
# print(dd[6])   잘못된 index 번호 오류

# 슬라이싱    ([시작값 :끝값+1 :건너뜀])
print(dd[1:4]) 
print(dd[1:4:2])  # 슬라이싱 할때 마지막 3번째 매개변수는 건너뜀
print(dd[:3])     # 시작값 생량 0부터 시작
print(dd[5:])     # 종료값 끝까지

aa = [1, 2, 3]
bb = [10, 20, 30]
print(aa + bb)    # 리스트 aa와 bb를 연결
print(aa * 5)     # aa 리스트를 5번 연결

aa[2] = 30
print(aa)

# 리스트 조작 함수  
# append() : 리스트의 맨 뒤에 항목 추가   , 리스트명.append(추가할값)
aa.append(5)
print(aa)

# pop() : 리스트에서 맨 뒤 항목 삭제 , 리스트명.pop()
aa.pop()
print(aa)

# insert() : 지정된 위치에 값을 삽이한다, 리스트명.insert(위치, 값)
aa.insert(1, -2)
print(aa)

# index() : 지정된 값의 index 반환 , 리스트명.index(찾을값)
print(aa.index(-2))

# remove() : 리스트에서 지정된 값 삭제. 지정된 값이 여러개면 첫번째 값만 지움
# 리스트명.remove(값)
aa.remove(-2)
print(aa)

# count() : 리스트에서 해당 값의 갯수 셈. 리스트명.count(찾을값)
aa.insert(2, 1)
print(aa)
print(aa.count(1))


# del() : 리스트에서 해당 index의 항목 삭제 . del(리스트명[위치])
del(aa[1])
print(aa)

# len() : 해당 리스트의 전체 항목 갯수 세기, len(리스트명)
print(len(aa))

# 리스트 컴프리헨션(단축수식)
list3 = [i*5 for i in range(5)]
print(list3)

# 3의 배수를 갖는 리스트를 원소 7개 만들기
list4 = [i*3 for i in range(1, 8)] 
print(list4)

# 2차원리스트 : 리스트 안에 또다른 리스트를 넣는 것으로 다차원리스트를 만들 수 있다
aa = [[10, 20, 30], [1, 2, 3], [1.1, 2.2, 3.3]]
print(aa[1][2])   # 1행 1열
print(aa[2][1])   
print(aa[0][2])

bb = [[1, 2, 3, 4],
      [5, 6],
      [7, 8, 9]]
print(bb)
