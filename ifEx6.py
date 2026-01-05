# 리스트에서의 if문 활용
# 리스트(list) : 데이터 여러개를 하나의 변수에 함께 저장한 형태

fruits = ['수박', '참외', '배', '포도', '딸기']
print(fruits)
print(fruits[3])

# fruits라는 리스트에 어떤 원소가 있는지 없는지 판별한다면..
if '사과' in fruits:
  print("사과가 있습니다")
else :
  print("사과가 없습니다")