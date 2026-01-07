# 문자열 처리 함수
str1 = '파이썬 ' * 3
print(str1)

# len 속성이 있다. 문자열의 길이를 구할 수 있다
print(len(str1))


# 대문자 소문자 변환 : upper(), lower(), swapcase(), title()
str1 = 'Python is Easy. 그래서 Programming이 재미있습니다'
print(str1.upper())
print(str1.lower())
print(str1.swapcase())
print(str1.title())

# 문자열 찾기 : count(), find(), rfind(), index(), rindex(), startwith(), endswith()
str2 = '파이썬 공부는 즐겁습니다. 물론 공부가 모두 재미있지는 않아요'
print(str2.count('공부'))   # 2
print(str2.find('공부'))    # 4, 왼쪽부터 찾기 시작하여 찾는 글자의 index값 반환. 못찾으면 -1반환
print(str2.rfind('공부'))   # 18, 오른쪽 부터 찾기 시작하여 첫번째 index값
# index와 find는 비슷하다. 하지만 index는 찾을 문자열이 없다면 오류가 난다.
print(str2.find('마이썬'))
# print(str2.index('마이썬')) 오류
print(str2.index('공부'))

str3 = 'student_name'
print(str3.startswith('student'))   # True

str4 = 'ifEx5.py'
print(str4.endswith('png'))

# 문자열 공백 삭제, 변경하기 : strip(), rstrip(), lstrip(), replace()
# 앞뒤 공백이나 특정 문자 삭제하려면 strip(), rstrip(), lstrip() < 중간에 있는 공백은 삭제 x
str5 = '  파  이  썬    '
print(str5.strip())
print(str5.rstrip())
print(str5.lstrip())

str6 = '$$파이썬$$'
print(str6.strip('$'))

# str5의 모든 공백 삭제 하여 출력하세요
newStr5 = ''
for ch in str5:
  if ch != ' ':
    newStr5 += ch
print(newStr5)

# replace를 이용하여 공백을 제거할 수도 있다.
print(str5.replace(" ", ""))

# 문자열 분리, 결합하기
# split() : 문자열을 공백이나 다른문자로 분리하여 리스트로 반환한다,
str6 = 'operator.py'
print(str6.split('.'))
# join() : 문자열 결합
str7 = '*'
print(str7.join('abc'))

# 전화번호를 입력받아 중간 4글자를 #으로 바꾸기
mobile = input("전화번호를 입력하세요 >>")
tmpMobileList = mobile.split('-')
print(tmpMobileList[0] + '-####-' + tmpMobileList[2])

