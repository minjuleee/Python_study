# 오늘 점심 뭐먹지
import random

menu = ['짜장면', '짬뽕', '김치찌개', '돈가스', '한식 뷔페', '도시락', '부대찌개']
num = random.randrange(1, 8)
print("오늘의 점심은 ", menu[num], "입니다")