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
# if stu_num[1]=='1' or stu_num[1]=='2':
#     gwa = '뉴미디어소프트웨어과'
# elif stu_num[1]=='3' or stu_num[1]=='4':
#     gwa = '뉴미디어웹솔루션과'
# elif stu_num[1]=='5' or stu_num[1]=='6':
#     gwa = '뉴미디어디자인과'
# else:
#     gwa = '존재하지 않는 학과'
#
# print(f'{stu_num[0]}학년 {stu_num[1]}반 {gwa} {stu_num[2:]}번')
# print(f'{stu_num[0]}학년 {stu_num[1]}반 {gwa} {stu_num[3]}번')

#이프문 안쓰고
# majors = ['', '뉴미디어소프트웨어과', '뉴미디어소프트웨어과','뉴미디어웹솔루션과', '뉴미디어웹솔루션과', '뉴미디어디자인과', '뉴미디어디자인과']
# index = int(stu_num[1])
# g = majors[index]

print('-'*30)

#입력하면 끝까지 더함
su = input()
sum1 = 0
for i in range(0,len(su),1):
    sum1 = sum1 + int(su[i])
print(sum1)

for number in range(1,100+1):
    number_s = str(number)
    for ch in number_s:
        if ch == '3' or ch == '6' or ch == '9':
            print('짝')
        else:
            print(ch, end='')
    print()

count = 0
for number in range(1,100+1):
    if ch == '3' or ch == '6' or ch == '9':
       count += 1

if count == 0:
    print(number)
else:
    print('짝'* count)