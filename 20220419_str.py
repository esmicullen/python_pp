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

