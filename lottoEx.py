# 1 ~ 45까지의 랜덤한 수 6개를 출력하여 로또 번호를 발생 시키는 프로그램
# 단, 한번 나왔던 값은 다시 나올 수 없다.
# 단, 로또 추첨이 되었던 번호인지 아닌지 판단하는 함수 isDuplication()를 작성하여,
# 그 함수를 이용하는 방식으로 프로그램을 작성하세요.

import random
# for i in range(2, 101, 2):
def isDuplicate(num):
  i = 0
  while i < len(lotto) :
    if lotto[i] == num:
      return True
    i += 1
  return False
  
  # for i in range(len(lotto)):
  #   if num == lotto[i]:
  #     return True
  # return False

lotto = []  # 로또 번호 저장될 리스트

while len(lotto) < 6 :  # 로또 번호가 6개가 저장될 때 까지 반복
  num = random.randint(1, 45)   # 1 ~ 45까지의 랜덤 번호 추첨
  print(isDuplicate(num))
  if isDuplicate(num):
    continue
  else :  # 중복되지 않음
    lotto.append(num)   # 저장

lotto.sort()
print('이번 주 로또 번호는 : ', lotto)
  


# def isDuplication(newLotto, lottoList):
#   for lotto in lottoList:
#     if newLotto == lotto:
#       return True
#     else:
#       return False


# def lotto():
#   i = 0
#   newLotto = 0
#   lottoList = []
#   while len(lottoList) < 6:
#     newLotto = random.randint(1, 45)
#     if isDuplication(newLotto, lottoList) == True:
#       continue
#     else :
#       lottoList.append(newLotto)
#     i += 1
#   return lottoList
    

# print(lotto())
