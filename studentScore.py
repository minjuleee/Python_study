score = [[1, '홍길동', 56, 32, 100],
          [2, '둘리', 33, 24, 55],
          [3, '도우너', 77, 88, 99],
          [4, '또치', 64, 32, 100]]


sum = [score[0][2] + score[0][3] + score[0][4]
       , score[1][2] + score[1][3] + score[1][4]
       , score[2][2] + score[2][3] + score[2][4]]

avg = [int(sum[0]/3), int(sum[1]/3), int(sum[2]/3)]

grade = []

for i in range(0, 3, 1):
  if avg[i] >= 90:
    grade.append('A')
  
  elif avg[i] >= 80 :
    grade.append('B')
  
  elif avg[i] >= 70:
    grade.append('C')
  
  elif avg[i] >= 60:
    grade.append('D')
  
  else :
    grade.append('F')
  

target = int(input("성적을 조회하고 싶은 번호를 입력하세요 >> "))
print(f"이름: {score[target-1][1]}, 합계: {sum[target-1]}, 평균: {avg[target-1]}, 학점: {grade[target-1]}")


