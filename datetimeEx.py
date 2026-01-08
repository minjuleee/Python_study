# 날짜를 사용자에게 입력 받는다. (년(4자리)/월/일 형식)
# 오늘 날짜까지 몇일 지났는지 출력한다.
from datetime import datetime, date, time, timedelta

userInputStr = input('날짜 입력 (년(4자리)/월/일 형식)')
print(userInputStr)

tmpList = userInputStr.split('/')
print(tmpList)

userInputDate = date(int(tmpList[0]), int(tmpList[1]), int(tmpList[2]))
print(userInputDate)

today = date.today()

print((today - userInputDate).days, "일 지났습니다!")

# dt = input("날짜를 입력해주세요 (YYYY/MM/DD)>> ")
# tmpList = dt.split('/')
# d = date(int(tmpList[0]), int(tmpList[1]), int(tmpList[2]))
# now = date.today()

# print((now - d).days)