greeting = 'hello'
to = 'world'

say_hello = greeting +', ' + to
print(say_hello)
print(greeting * 5)
print(greeting + '\n' + to)
print("\"" + greeting + "\"")
print('\'' + greeting + '\'')

names = '양다연인소리이예진'

print(names[2]) #연
print(names[4]) #소
print(names[8]) #진

print(names[-1]) #진
print(names[-2]) #예
print(names[-9]) #양

# *** indexing, slicing

stu_num = '2112'
print(stu_num[0] + '학년')
print(f'{stu_num[0]}학년')
print(f'{stu_num[1]}반')

#'양다연인소리이예진'
print(names[2:5])
print(names[2]+names[3])

print(f'{stu_num[2:4]}번')
print(f'{stu_num[0:]}번') #start:end-1 [start:]: 끝까지
print(f'{stu_num[:-2]}번') #start:end-1 [:end-1]: 앞까지
print(f'{stu_num[:]}번') #start:end-1 [:]: 앞~끝까지

#문자열 함수
print(f'길이: {len(stu_num)}') #4
print(f'2개수: {stu_num.count("2")}') #2
print(f'{"seventeen darling".upper()}')
print(f'{"seventeen darling".lower()}')
s = "   NCT dream buffering   "
print(f'{s.strip()}')
print(f'{s.lstrip()}')
print(f'{s.rstrip()}')
print(f'{s.find("d")}')
#print(f'{s.find("z")}') #없으면 에러
print(f'{s.replace("buffering","hello future")}')
print(s)

print('e' in s)
print('z' in s)

#split, join
ip = '10.253.123.119'
ip_list=ip.split('.')
print(ip_list)
names = '양다연,최자윤,임채영,이예진,인소리'
name_list = names.split(',')
print(name_list)
print(name_list[2])
print(name_list[2:4])
ip_list_str = '::'.join(ip_list)
print(ip_list_str)
name_list_str = '|'.join(name_list)
print(name_list_str)

#format
s = 'name: {},number: {}, soccer: {}'
print(format('손흥민', 7, True))

s = 'name: {1},number: {2}, soccer: {0}'
print(format('손흥민', 7, True))

s = 'name: {name},number: {n}, soccer: {s}'
#print(format(name='손흥민', n=7, s=True))
#46 연습

