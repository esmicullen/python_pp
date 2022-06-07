# #휴대전화 번호 입력시 -,/,띄어쓰기 없애고 숫자만 출력
#
# phone_num = "010-7240-4658"
# print(phone_num.replace('-',''))
# phone_num = "010/7240/4658"
# print(phone_num.replace('/',''))
# phone_num = "010 7240 4658"
# print(phone_num.replace(' ',''))
#
# print('-'*17)
#
# #학번 -> 학년, 반, 학과, 번호 출력
# stu_num = input()
# gwa = ''
# if stu_num[0]=='1' or stu_num[0]=='2':
#     gwa = '뉴미디어소프트웨어과'
# elif stu_num[0]=='3' or stu_num[0]=='4':
#     gwa = '뉴미디어솔루션과'
# elif stu_num[0]=='5' or stu_num[0]=='6':
#     gwa = '뉴미디어디자인과'
# else:
#     gwa = '존재하지 않는 학과'
#
# print(f'{stu_num[0]}학년 {stu_num[1]}반 {gwa} {stu_num[2:]}번')
# print(f'{stu_num[0]}학년 {stu_num[1]}반 {gwa} {stu_num[3]}번')

#이프문 안쓰고

print('-'*30)

#입력하면 끝까지 더함
su = input()
sum = 0
for i in range(0,len(su),1):
    sum = sum + int(su[i])
print(sum)