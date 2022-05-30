# #교통수단 문제
# money = int(input('돈을 입력해주세요 : '))
# if money >= 10000:
#     print('택시 탑승')
# elif money >= 720:
#     print('버스 탑승')
# else:
#     print('도보 걷기')

# num = int(input('정수를 입력해주시술 : '))
# if num % 4 == 0:
#     print(f'{num} is 4의 배수입니다')
# elif num % 3 == 0:
#     print(f'{num} is 3의 배수입니다')
# elif num % 2 == 0:
#     print(f'{num} is 2의 배수입니다')
# else:
#     print(f'{num} is 아무것도 아닙니다')
# #만약 elif가 아닌 if로 묶여있을 경우 각자 다 다른 if문임!
#

#age = int(input('나이 입력 : '))
# if 10 <= age < 20:
#     print('십대 입니다')
# elif 30 <= age < 40:
#     print('삼십대 입니다')
# else:
#     print('둘 다 아닙니다')
#print(f'{age//10}0대 입니다')

# x = int(input('정수 입력 : '))
#
# if x > 10 and x % 2 == 0:
#     print(f'{x}는 10 초과 짝수')

# j = int(input('점수 입력 : '))
#
# if 100 >= j >= 90:
#     print('A')
# elif 90 > j >= 80:
#     print('B')
# elif 80 > j >= 70:
#     print('C')
# elif 70 > j >= 60:
#     print('D')
# elif 60 > j >= 0:
#     print('F')
#
# MBTI = input('MBTI가 뭐묘? >> ')
# if MBTI.upper() == "ENTP":
#     print("iOS형")
# elif MBTI.upper() == "INTP":
#     print("백엔드형")
# else:
#     print("아직 개발중임")
#

# x = int(input('정수 입력 : '))
# if x > 10:
#     if x % 2 == 0:
#         print(f'{x}는 10 초과 짝수')
#     else:
#         print(f'{x}는 10 초과 홀수')
# elif x <= 10:
#     print(f'{x}는 10 이하')

print("----[초기 설정]----")
nick = input('사용자 이름 설정 : ')
nid = input('아이디를 설정해주세요 : ')
password = input('비밀번호를 설정해주세요 : ')

print("----[로그인 화면]----")

reid = input('아이디를 입력해주세요 : ')
repassword = input('비밀번호를 입력해주세요 : ')

if nid == reid:
    if password == repassword:
        print(f'모두 일치. {nick}님 환영합니다')
    else:
        print('패스워드 불일치')
else:
    print('아이디 불일치, How are you?')
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")