# if ~ elif ~ else 문

name = input("이름을 입력 >> ")
kor = int(input("국어 점수 >>"))
eng = int(input("영어 점수 >>"))
math = int(input("수학 점수 >>"))

tot = kor + eng + math
avg = tot / 3
grade = ''

if avg >= 90 :
  grade = '수'
elif avg >= 80 :
  grade = '우'
elif avg >= 70 :
  grade = '미'
elif avg >= 60 :
  grade = '양'
else : 
  grade = '가'

print("이름 : ", name)
print("국어 : ", kor)
print("영어 : ", eng)
print("수학 : ", math)
print("총점 : ", tot)
print("평균 : ", avg)
print("학점 : ", grade)

