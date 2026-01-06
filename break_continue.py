# continue (현재 반복 중지하고 다음 loop로 skip)
# for i in range(3) : # i = 0, 1, 2
#   if i == 1:
#     continue
#   else :
#     print(i)

# break 문 : 반복문 종료
i = 1
sum = 0
while True :
  sum += i
  i += 1
  if sum >= 1000 :
    break

print(i)

  