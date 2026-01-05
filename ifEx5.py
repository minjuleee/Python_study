# 3항 연산자를 이용한 if문
# : 조건에 다라 서로 다른 값을 변수에 대입할 때 사용ㅎ나다

userInput = input("성별을 입력하세요 (M/F) ?")
if userInput == 'M' or 'm' :
    result = '남자'
else : 
  result = '여자'
  
print(result)