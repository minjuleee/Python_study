# 연도를 입력 받아 입력 받은 연도가 윤년인지 아닌지
# 윤년 : 4로 나누어 떨어지고, 100으로 나누어 떨어지지 않으면 윤년이다.
#     : 400으로 나누어 떨어지는 해도 윤년이다

user_input = 0
# 연도를 유저에게 입력받는다
user_input = int(input("연도를 입력하세요 >> "))

# 윤년인지 아닌지  비교 판단한다
if (user_input % 4 == 0 and user_input % 100 != 0) or (user_input % 400 == 0) : 
    # 참일때
    print(str(user_input) + "년은 윤년입니다.")
else : 
    # 거짓일때
    print(str(user_input) + "년은 윤년이 아닙니다.")
# 결과를 출력한다


# if 조건식 :
#    조건식이 참일 때 수행되는 문장(들)
# else :
#    조건식이 거짓일 때 수행되는 문장(들)


# testYear = int(input("년도를 입력해주세요 >> "))
# if(testYear % 4 == 0 and testYear % 100 != 0) or (testYear % 400 == 0):
#   print("윤년입니다.")

# elif (testYear % 400 == 0):
#   print("윤년입니다.")

# else : print("윤년이 아닙니다.")