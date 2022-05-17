'''
조건식 = true or False로 결정되는 문장
파이썬에서 if문 작성시 유의해야 할 사항 - 콜론, 들여쓰기
'''
#if True :
#    print('실행')
# #교통수단 결정 문제
# money = 15000
# if money >= 10000:
#     print('택시 탑승')
# else:
#     print('버스 탑승')
#
# #input함수
# x = input()
# print(x, type(x))
# num = int(input())
# print(num, type(num))

# #교통수단 결정 문제 + input
# money = int(input('돈을 입력하시오 : '))
# if money >= 10000:
#     print('택시 탑승')
# else:
#     print('버스 탑승')

# num = int(input('숫자를 입력하세요 : '))
# if num%2==0:
#     print(f'{num}은/는 짝수입니다')
# else:
#     print(f'{num}은/는 홀수입니다')
#

password = input('비밀번호를 설정해주세요 : ')
repass = input('비밀번호를 다시 입력해주세요 : ')
if password == repass:
    print("일치")
else:
    print("불일치")