# set : 딕셔너리에서 키부분만 있는 자료형
# 중복되지 않은 값들로 구성되며, 순서가 없다 (인덱스가 없다)

nums = [1, 2, 2, 3, 3]
unique = list(set(nums))
print(nums, unique)

# set은 집합 연산을 제공한다
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))   # 합집합
print(a.intersection(b))   # 교집합
print(a.difference(b))     # 차집합
print(a.symmetric_difference(b))  # 대칭차 (서로 다른거)