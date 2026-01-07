# shallow copy(얕은 복사) : 같은 주소값을 참조(같은 객체)하기 때문에,
# 원본이나 사본 둘중의 하나를 변경하면, 값이 같이 변경
oldList = ['짜장면', '군만두', '탕수육']
newList = oldList
print(newList)

newList[0] = '짬뽕'
print(newList, oldList)

# deep copy(깊은 복사) : 새로운 리스트를 만들어서(다른 주소값)
oldList2 = ['짜장면', '군만두', '탕수육']
newList2 = oldList2[:]
print(newList2, oldList2)
oldList2[0] = '짬뽕'
print(newList2, oldList2)