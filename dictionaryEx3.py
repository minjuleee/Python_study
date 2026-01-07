# 물건을 수송하는 기차 여러 대의 수송량을 합산하여 순위를 매기는 프로그램을 작성하세요.

import operator

trainTupleList = [('토마스', 5), ('헨리', 8), ('에드워드', 9), ('에밀리', 5),
                  ('토마스', 4), ('헨리', 7), ('토마스', 3), ('에밀리', 8),
                  ('퍼시', 5), ('고든', 13),]

trainDict, trainList = {}, []
tmpTuple = None
totalRank, curRank = 1, 1   # 등수 매기기 위한 변수


# 정렬을 시키기 위해 수송량을 합산
for tmpTuple in trainTupleList :
  tName = tmpTuple[0]
  tWeight = tmpTuple[1]
  if tName in trainDict :
    trainDict[tName] += tWeight # 기차이름이 존재한다면 수송량 누적
  else :
    trainDict[tName] = tWeight  # 기차가 없으면 수송량 대입
    
print('기차 수송량 ')
trainList = sorted(trainDict.items(), key=operator.itemgetter(1), reverse=True)
# print(trainList)
# 등수 매기기 : (내림차순 정렬을 했기 때문에) 0번째 요소는 무조건 1등이다.
# 다음 기차의 수송량이 바로 앞 기차의 수송량과 같다면. curRank 유지(공동순위)
# 다음 기차의 수송량이 바로 앞 기차의 수송량과 다르다면 totalRank를 1증가시켜서 이 값으로 갱신

print('기차 이름 \t 총 수송량 \t 순위')
print('----------------------------------------------')
print(trainList[0][0], '\t\t', trainList[0][1], '\t\t\t', curRank)

for i in range(1, len(trainList)):
  totalRank += 1
  if trainList[i][1] == trainList[i-1][1]:   # 앞 기차와 수송량이 같다면
    pass  # 수행할 코드 없음
  else :
    curRank = totalRank
  
  print(trainList[i][0], '\t\t', trainList[i][1], '\t\t\t', curRank)
    



